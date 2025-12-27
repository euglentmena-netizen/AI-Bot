"""
Financial Data Extraction Module
Extracts financial statements from Excel and PDF files
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional


class FinancialDataExtractor:
    """Extract financial data from Excel and PDF files"""
    
    def __init__(self, file_obj, file_type: str):
        """
        Initialize extractor
        
        Args:
            file_obj: File object (Excel or PDF)
            file_type: 'excel' or 'pdf'
        """
        self.file_obj = file_obj
        self.file_type = file_type
        self.data = {}
    
    def extract_from_excel(self, sheet_names: Optional[List[str]] = None) -> Dict:
        """Extract financial data from Excel file"""
        
        excel_file = pd.ExcelFile(self.file_obj)
        
        if sheet_names is None:
            sheet_names = excel_file.sheet_names
        
        extracted_data = {}
        
        for sheet in sheet_names:
            df = pd.read_excel(self.file_obj, sheet_name=sheet)
            extracted_data[sheet] = df
            
            # Auto-detect financial statement type
            if self._is_income_statement(df):
                self.data['income_statement'] = self._parse_income_statement(df)
            elif self._is_balance_sheet(df):
                self.data['balance_sheet'] = self._parse_balance_sheet(df)
            elif self._is_cash_flow(df):
                self.data['cash_flow'] = self._parse_cash_flow(df)
        
        return extracted_data
    
    def extract_from_pdf(self) -> Dict:
        """Extract financial data from PDF file"""
        
        try:
            import pdfplumber
            
            extracted_data = {}
            
            with pdfplumber.open(self.file_obj) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    
                    for table_idx, table in enumerate(tables):
                        df = pd.DataFrame(table)
                        
                        # Clean headers
                        df.columns = [str(col).strip() for col in df.iloc[0]]
                        df = df[1:].reset_index(drop=True)
                        
                        # Detect statement type
                        if self._is_income_statement(df):
                            self.data['income_statement'] = self._parse_income_statement(df)
                        elif self._is_balance_sheet(df):
                            self.data['balance_sheet'] = self._parse_balance_sheet(df)
                        elif self._is_cash_flow(df):
                            self.data['cash_flow'] = self._parse_cash_flow(df)
                        
                        extracted_data[f'page_{page_num}_table_{table_idx}'] = df
            
            return extracted_data
        
        except ImportError:
            raise ImportError("pdfplumber is required for PDF extraction. Install with: pip install pdfplumber")
    
    def _is_income_statement(self, df: pd.DataFrame) -> bool:
        """Check if dataframe is an income statement"""
        
        key_terms = ['revenue', 'sales', 'cost of revenue', 'gross profit', 
                     'operating income', 'net income', 'earnings']
        
        text = ' '.join(df.astype(str).values.flatten()).lower()
        
        matched_terms = sum(1 for term in key_terms if term in text)
        
        return matched_terms >= 3
    
    def _is_balance_sheet(self, df: pd.DataFrame) -> bool:
        """Check if dataframe is a balance sheet"""
        
        key_terms = ['assets', 'liabilities', 'equity', 'shareholders',
                     'current assets', 'fixed assets', 'accounts payable']
        
        text = ' '.join(df.astype(str).values.flatten()).lower()
        
        matched_terms = sum(1 for term in key_terms if term in text)
        
        return matched_terms >= 2
    
    def _is_cash_flow(self, df: pd.DataFrame) -> bool:
        """Check if dataframe is a cash flow statement"""
        
        key_terms = ['operating activities', 'investing activities', 
                     'financing activities', 'cash flow', 'cash provided']
        
        text = ' '.join(df.astype(str).values.flatten()).lower()
        
        matched_terms = sum(1 for term in key_terms if term in text)
        
        return matched_terms >= 2
    
    def _parse_income_statement(self, df: pd.DataFrame) -> Dict:
        """Parse income statement data"""
        
        parsed = {
            'revenue': self._find_numeric_value(df, ['revenue', 'net sales', 'total revenue']),
            'cost_of_revenue': self._find_numeric_value(df, ['cost of revenue', 'cost of goods sold', 'cogs']),
            'gross_profit': self._find_numeric_value(df, ['gross profit', 'gross margin']),
            'operating_expenses': self._find_numeric_value(df, ['operating expenses', 'opex']),
            'operating_income': self._find_numeric_value(df, ['operating income', 'operating profit', 'ebit']),
            'interest_expense': self._find_numeric_value(df, ['interest expense', 'interest paid']),
            'tax_expense': self._find_numeric_value(df, ['income tax expense', 'tax expense']),
            'net_income': self._find_numeric_value(df, ['net income', 'net profit', 'bottom line']),
            'eps': self._find_numeric_value(df, ['earnings per share', 'eps', 'basic eps'])
        }
        
        return {k: v for k, v in parsed.items() if v is not None}
    
    def _parse_balance_sheet(self, df: pd.DataFrame) -> Dict:
        """Parse balance sheet data"""
        
        parsed = {
            'current_assets': self._find_numeric_value(df, ['current assets', 'total current assets']),
            'total_assets': self._find_numeric_value(df, ['total assets']),
            'current_liabilities': self._find_numeric_value(df, ['current liabilities', 'total current liabilities']),
            'total_liabilities': self._find_numeric_value(df, ['total liabilities']),
            'shareholders_equity': self._find_numeric_value(df, ['shareholders equity', 'total equity', 'stockholders equity']),
            'cash': self._find_numeric_value(df, ['cash', 'cash and equivalents']),
            'accounts_receivable': self._find_numeric_value(df, ['accounts receivable']),
            'inventory': self._find_numeric_value(df, ['inventory']),
            'ppe': self._find_numeric_value(df, ['property plant equipment', 'ppe', 'fixed assets']),
            'accounts_payable': self._find_numeric_value(df, ['accounts payable']),
            'long_term_debt': self._find_numeric_value(df, ['long term debt', 'long-term debt'])
        }
        
        return {k: v for k, v in parsed.items() if v is not None}
    
    def _parse_cash_flow(self, df: pd.DataFrame) -> Dict:
        """Parse cash flow statement data"""
        
        parsed = {
            'operating_cash_flow': self._find_numeric_value(df, ['operating cash flow', 'cash from operations']),
            'investing_cash_flow': self._find_numeric_value(df, ['investing cash flow', 'cash from investing']),
            'financing_cash_flow': self._find_numeric_value(df, ['financing cash flow', 'cash from financing']),
            'capital_expenditure': self._find_numeric_value(df, ['capital expenditure', 'capex']),
            'free_cash_flow': self._find_numeric_value(df, ['free cash flow', 'fcf']),
            'dividend_paid': self._find_numeric_value(df, ['dividends paid', 'dividend paid'])
        }
        
        return {k: v for k, v in parsed.items() if v is not None}
    
    def _find_numeric_value(self, df: pd.DataFrame, search_terms: List[str]) -> Optional[float]:
        """Find numeric value matching search terms"""
        
        for idx, row in df.iterrows():
            row_text = ' '.join(str(val).lower() for val in row)
            
            for term in search_terms:
                if term.lower() in row_text:
                    # Try to find numeric value in the same row
                    for val in row:
                        try:
                            numeric_val = float(val)
                            if numeric_val != 0:  # Avoid zero values
                                return numeric_val
                        except (ValueError, TypeError):
                            continue
        
        return None
    
    def get_extracted_data(self) -> Dict:
        """Get all extracted data"""
        return self.data


class FinancialAnalyzer:
    """Calculate financial metrics and KPIs"""
    
    def __init__(self, income_stmt: Dict, balance_sheet: Dict, cash_flow: Dict = None):
        """
        Initialize analyzer
        
        Args:
            income_stmt: Parsed income statement data
            balance_sheet: Parsed balance sheet data
            cash_flow: Parsed cash flow data (optional)
        """
        self.income_stmt = income_stmt
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow or {}
    
    def calculate_profitability_ratios(self) -> Dict[str, float]:
        """Calculate profitability ratios"""
        
        ratios = {}
        
        # Gross Profit Margin
        if 'revenue' in self.income_stmt and 'cost_of_revenue' in self.income_stmt:
            gross_profit = self.income_stmt['revenue'] - self.income_stmt['cost_of_revenue']
            ratios['gross_profit_margin'] = (gross_profit / self.income_stmt['revenue']) * 100
        
        # Operating Profit Margin
        if 'revenue' in self.income_stmt and 'operating_income' in self.income_stmt:
            ratios['operating_margin'] = (self.income_stmt['operating_income'] / self.income_stmt['revenue']) * 100
        
        # Net Profit Margin
        if 'revenue' in self.income_stmt and 'net_income' in self.income_stmt:
            ratios['net_profit_margin'] = (self.income_stmt['net_income'] / self.income_stmt['revenue']) * 100
        
        # Return on Assets (ROA)
        if 'net_income' in self.income_stmt and 'total_assets' in self.balance_sheet:
            ratios['roa'] = (self.income_stmt['net_income'] / self.balance_sheet['total_assets']) * 100
        
        # Return on Equity (ROE)
        if 'net_income' in self.income_stmt and 'shareholders_equity' in self.balance_sheet:
            if self.balance_sheet['shareholders_equity'] != 0:
                ratios['roe'] = (self.income_stmt['net_income'] / self.balance_sheet['shareholders_equity']) * 100
        
        return ratios
    
    def calculate_liquidity_ratios(self) -> Dict[str, float]:
        """Calculate liquidity ratios"""
        
        ratios = {}
        
        # Current Ratio
        if 'current_assets' in self.balance_sheet and 'current_liabilities' in self.balance_sheet:
            if self.balance_sheet['current_liabilities'] != 0:
                ratios['current_ratio'] = self.balance_sheet['current_assets'] / self.balance_sheet['current_liabilities']
        
        # Quick Ratio
        if 'current_assets' in self.balance_sheet and 'inventory' in self.balance_sheet and 'current_liabilities' in self.balance_sheet:
            quick_assets = self.balance_sheet['current_assets'] - self.balance_sheet.get('inventory', 0)
            if self.balance_sheet['current_liabilities'] != 0:
                ratios['quick_ratio'] = quick_assets / self.balance_sheet['current_liabilities']
        
        # Cash Ratio
        if 'cash' in self.balance_sheet and 'current_liabilities' in self.balance_sheet:
            if self.balance_sheet['current_liabilities'] != 0:
                ratios['cash_ratio'] = self.balance_sheet['cash'] / self.balance_sheet['current_liabilities']
        
        return ratios
    
    def calculate_efficiency_ratios(self) -> Dict[str, float]:
        """Calculate efficiency ratios"""
        
        ratios = {}
        
        # Asset Turnover
        if 'revenue' in self.income_stmt and 'total_assets' in self.balance_sheet:
            if self.balance_sheet['total_assets'] != 0:
                ratios['asset_turnover'] = self.income_stmt['revenue'] / self.balance_sheet['total_assets']
        
        # Receivables Turnover
        if 'revenue' in self.income_stmt and 'accounts_receivable' in self.balance_sheet:
            if self.balance_sheet['accounts_receivable'] != 0:
                ratios['receivables_turnover'] = self.income_stmt['revenue'] / self.balance_sheet['accounts_receivable']
        
        # Inventory Turnover
        if 'cost_of_revenue' in self.income_stmt and 'inventory' in self.balance_sheet:
            if self.balance_sheet['inventory'] != 0:
                ratios['inventory_turnover'] = self.income_stmt['cost_of_revenue'] / self.balance_sheet['inventory']
        
        return ratios
    
    def calculate_leverage_ratios(self) -> Dict[str, float]:
        """Calculate leverage/solvency ratios"""
        
        ratios = {}
        
        # Debt-to-Equity Ratio
        if 'total_liabilities' in self.balance_sheet and 'shareholders_equity' in self.balance_sheet:
            if self.balance_sheet['shareholders_equity'] != 0:
                ratios['debt_to_equity'] = self.balance_sheet['total_liabilities'] / self.balance_sheet['shareholders_equity']
        
        # Debt-to-Assets Ratio
        if 'total_liabilities' in self.balance_sheet and 'total_assets' in self.balance_sheet:
            if self.balance_sheet['total_assets'] != 0:
                ratios['debt_to_assets'] = self.balance_sheet['total_liabilities'] / self.balance_sheet['total_assets']
        
        # Equity Ratio
        if 'shareholders_equity' in self.balance_sheet and 'total_assets' in self.balance_sheet:
            if self.balance_sheet['total_assets'] != 0:
                ratios['equity_ratio'] = self.balance_sheet['shareholders_equity'] / self.balance_sheet['total_assets']
        
        # Interest Coverage Ratio
        if 'operating_income' in self.income_stmt and 'interest_expense' in self.income_stmt:
            if self.income_stmt['interest_expense'] != 0:
                ratios['interest_coverage'] = self.income_stmt['operating_income'] / self.income_stmt['interest_expense']
        
        return ratios
    
    def calculate_cash_flow_metrics(self) -> Dict[str, float]:
        """Calculate cash flow metrics"""
        
        metrics = {}
        
        if self.cash_flow:
            # Operating Cash Flow Margin
            if 'operating_cash_flow' in self.cash_flow and 'revenue' in self.income_stmt:
                metrics['ocf_margin'] = (self.cash_flow['operating_cash_flow'] / self.income_stmt['revenue']) * 100
            
            # Free Cash Flow
            if 'operating_cash_flow' in self.cash_flow and 'capital_expenditure' in self.cash_flow:
                fcf = self.cash_flow['operating_cash_flow'] - self.cash_flow['capital_expenditure']
                metrics['free_cash_flow'] = fcf
            
            # Cash Flow to Net Income
            if 'operating_cash_flow' in self.cash_flow and 'net_income' in self.income_stmt:
                metrics['cash_flow_to_ni'] = self.cash_flow['operating_cash_flow'] / self.income_stmt['net_income']
        
        return metrics
    
    def get_all_metrics(self) -> Dict:
        """Calculate and return all metrics"""
        
        return {
            'profitability': self.calculate_profitability_ratios(),
            'liquidity': self.calculate_liquidity_ratios(),
            'efficiency': self.calculate_efficiency_ratios(),
            'leverage': self.calculate_leverage_ratios(),
            'cash_flow': self.calculate_cash_flow_metrics()
        }
    
    def generate_summary(self) -> str:
        """Generate text summary of analysis"""
        
        metrics = self.get_all_metrics()
        summary = []
        
        summary.append("=" * 60)
        summary.append("FINANCIAL ANALYSIS SUMMARY")
        summary.append("=" * 60)
        
        summary.append("\nPROFITABILITY RATIOS:")
        for metric, value in metrics['profitability'].items():
            summary.append(f"  {metric}: {value:.2f}%")
        
        summary.append("\nLIQUIDITY RATIOS:")
        for metric, value in metrics['liquidity'].items():
            summary.append(f"  {metric}: {value:.2f}x")
        
        summary.append("\nEFFICIENCY RATIOS:")
        for metric, value in metrics['efficiency'].items():
            summary.append(f"  {metric}: {value:.2f}x")
        
        summary.append("\nLEVERAGE RATIOS:")
        for metric, value in metrics['leverage'].items():
            summary.append(f"  {metric}: {value:.2f}x")
        
        if metrics['cash_flow']:
            summary.append("\nCASH FLOW METRICS:")
            for metric, value in metrics['cash_flow'].items():
                summary.append(f"  {metric}: {value:.2f}")
        
        summary.append("=" * 60)
        
        return "\n".join(summary)
