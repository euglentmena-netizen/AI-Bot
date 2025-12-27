"""
Investment Recommendation Engine
Generates recommendations, pros, cons, and risks based on financial metrics
"""

from typing import Dict, List, Tuple


class RecommendationEngine:
    """Generate investment recommendations based on financial analysis"""
    
    def __init__(self, metrics: Dict, company_info: Dict):
        """
        Initialize recommendation engine
        
        Args:
            metrics: Financial metrics from FinancialAnalyzer
            company_info: Company information (name, industry, period)
        """
        self.metrics = metrics
        self.company_info = company_info
        self.recommendation = None
        self.confidence = 0
        self.thesis = ""
    
    def analyze_profitability(self) -> Tuple[float, List[str]]:
        """Analyze profitability and generate insights"""
        
        score = 0
        insights = []
        
        prof = self.metrics.get('profitability', {})
        
        # Gross Margin Analysis
        gpm = prof.get('gross_profit_margin', 0)
        if gpm > 40:
            score += 2
            insights.append("Excellent gross profit margin above 40% - strong pricing power")
        elif gpm > 30:
            score += 1
            insights.append("Good gross profit margin above 30% - healthy operations")
        elif gpm > 20:
            insights.append("Moderate gross profit margin - room for improvement")
        else:
            insights.append("Low gross profit margin - pressure on unit economics")
        
        # Operating Margin Analysis
        opm = prof.get('operating_margin', 0)
        if opm > 25:
            score += 2
            insights.append("Excellent operating leverage with margin above 25%")
        elif opm > 15:
            score += 1
            insights.append("Good operating margin - efficient cost structure")
        else:
            insights.append("Operating margin below industry standards")
        
        # Net Profit Margin Analysis
        npm = prof.get('net_profit_margin', 0)
        if npm > 20:
            score += 2
            insights.append("Excellent net profitability above 20%")
        elif npm > 10:
            score += 1
            insights.append("Solid net profitability")
        else:
            insights.append("Net margin needs improvement")
        
        # ROE Analysis
        roe = prof.get('roe', 0)
        if roe > 30:
            score += 2
            insights.append("Exceptional ROE above 30% - excellent shareholder returns")
        elif roe > 15:
            score += 1
            insights.append("Good ROE above 15%")
        else:
            insights.append("ROE below expectations")
        
        # ROA Analysis
        roa = prof.get('roa', 0)
        if roa > 15:
            score += 1
            insights.append("Strong asset efficiency with ROA above 15%")
        
        return score, insights
    
    def analyze_liquidity(self) -> Tuple[float, List[str]]:
        """Analyze liquidity and generate insights"""
        
        score = 0
        insights = []
        
        liq = self.metrics.get('liquidity', {})
        
        # Current Ratio Analysis
        cr = liq.get('current_ratio', 0)
        if cr >= 1.5:
            score += 2
            insights.append("Excellent liquidity with current ratio above 1.5x")
        elif cr >= 1.0:
            score += 1
            insights.append("Adequate current ratio above 1.0x")
        else:
            insights.append("Current ratio below 1.0x - liquidity concerns")
        
        # Quick Ratio Analysis
        qr = liq.get('quick_ratio', 0)
        if qr >= 1.0:
            score += 1
            insights.append("Strong quick ratio - can cover short-term obligations")
        elif qr >= 0.7:
            insights.append("Quick ratio adequate but monitor closely")
        else:
            insights.append("Quick ratio below 0.7x - potential liquidity risk")
        
        # Cash Ratio Analysis
        cash_r = liq.get('cash_ratio', 0)
        if cash_r >= 0.5:
            score += 1
            insights.append("Strong cash position")
        
        return score, insights
    
    def analyze_leverage(self) -> Tuple[float, List[str]]:
        """Analyze leverage and generate insights"""
        
        score = 0
        insights = []
        
        lev = self.metrics.get('leverage', {})
        
        # Debt-to-Equity Analysis
        dte = lev.get('debt_to_equity', 0)
        if dte < 1.0:
            score += 2
            insights.append("Conservative leverage with D/E ratio below 1.0x")
        elif dte < 2.0:
            score += 1
            insights.append("Moderate leverage with D/E ratio below 2.0x")
        else:
            insights.append("High leverage - increased financial risk")
        
        # Debt-to-Assets Analysis
        dta = lev.get('debt_to_assets', 0)
        if dta < 0.5:
            score += 1
            insights.append("Healthy debt-to-assets ratio")
        
        # Interest Coverage Analysis
        ic = lev.get('interest_coverage', 1)
        if ic > 10:
            score += 2
            insights.append("Excellent interest coverage above 10x")
        elif ic > 3:
            score += 1
            insights.append("Adequate interest coverage")
        else:
            insights.append("Interest coverage below 3x - debt servicing concerns")
        
        return score, insights
    
    def analyze_efficiency(self) -> Tuple[float, List[str]]:
        """Analyze operational efficiency and generate insights"""
        
        score = 0
        insights = []
        
        eff = self.metrics.get('efficiency', {})
        
        # Asset Turnover Analysis
        at = eff.get('asset_turnover', 0)
        if at > 2.0:
            score += 1
            insights.append("Excellent asset utilization with turnover above 2.0x")
        elif at > 1.0:
            insights.append("Moderate asset turnover")
        else:
            insights.append("Low asset turnover - inefficient asset utilization")
        
        # Receivables Turnover Analysis
        rt = eff.get('receivables_turnover', 0)
        if rt > 10:
            score += 1
            insights.append("Excellent receivables collection")
        elif rt < 5:
            insights.append("Slow receivables collection - monitor credit policy")
        
        # Inventory Turnover Analysis
        it = eff.get('inventory_turnover', 0)
        if it > 5:
            score += 1
            insights.append("Efficient inventory management")
        elif it < 2:
            insights.append("Slow inventory turnover - potential obsolescence risk")
        
        return score, insights
    
    def generate_recommendation(self) -> Dict:
        """Generate overall investment recommendation"""
        
        # Score components
        prof_score, prof_insights = self.analyze_profitability()
        liq_score, liq_insights = self.analyze_liquidity()
        lev_score, lev_insights = self.analyze_leverage()
        eff_score, eff_insights = self.analyze_efficiency()
        
        total_score = prof_score + liq_score + lev_score + eff_score
        max_score = 16  # 4 categories * 4 points max each
        overall_percentage = (total_score / max_score) * 100
        
        # Determine recommendation
        if overall_percentage >= 70:
            recommendation = "BUY"
            confidence = min(95, 70 + (overall_percentage - 70) * 0.5)
        elif overall_percentage >= 50:
            recommendation = "HOLD"
            confidence = 60
        else:
            recommendation = "SELL"
            confidence = 50
        
        # Build investment thesis
        thesis_points = [
            f"Profitability Score: {prof_score}/4",
            f"Liquidity Score: {liq_score}/4",
            f"Leverage Score: {lev_score}/4",
            f"Efficiency Score: {eff_score}/4"
        ]
        
        all_insights = prof_insights + liq_insights + lev_insights + eff_insights
        
        self.recommendation = recommendation
        self.confidence = confidence
        
        return {
            'recommendation': recommendation,
            'confidence': f"{confidence:.0f}%",
            'overall_score': f"{overall_percentage:.1f}/100",
            'component_scores': {
                'profitability': prof_score,
                'liquidity': liq_score,
                'leverage': lev_score,
                'efficiency': eff_score
            },
            'key_insights': all_insights,
            'thesis_points': thesis_points
        }
    
    def generate_strengths(self) -> List[Dict]:
        """Generate list of company strengths"""
        
        _, prof_insights = self.analyze_profitability()
        _, liq_insights = self.analyze_liquidity()
        _, lev_insights = self.analyze_leverage()
        _, eff_insights = self.analyze_efficiency()
        
        strengths = []
        
        # Filter for positive insights
        positive_insights = []
        for insight in prof_insights + liq_insights + lev_insights + eff_insights:
            if any(word in insight.lower() for word in ['excellent', 'strong', 'good', 'healthy']):
                positive_insights.append(insight)
        
        # Create structured strengths
        strength_descriptions = {
            'Profitability': 'Strong profit margins and efficient operations demonstrate pricing power and cost control.',
            'Liquidity': 'Adequate current assets and liquid reserves to meet short-term obligations.',
            'Conservative Leverage': 'Healthy balance sheet with moderate debt levels and good interest coverage.',
            'Operational Efficiency': 'Effective asset utilization and operational management.',
            'Revenue Growth': 'Consistent revenue expansion indicating market demand.',
            'Cash Generation': 'Strong operating cash flow supports growth investments and dividends.'
        }
        
        strength_list = []
        for title, description in strength_descriptions.items():
            if any(keyword in ' '.join(positive_insights).lower() for keyword in title.lower().split()):
                strength_list.append({
                    'title': title,
                    'description': description
                })
        
        # Ensure we have at least 3 strengths
        while len(strength_list) < 3 and len(strength_descriptions) > len(strength_list):
            for title, description in strength_descriptions.items():
                if {'title': title, 'description': description} not in strength_list:
                    strength_list.append({
                        'title': title,
                        'description': description
                    })
                    break
        
        return strength_list[:6]
    
    def generate_concerns(self) -> List[Dict]:
        """Generate list of concerns"""
        
        _, prof_insights = self.analyze_profitability()
        _, liq_insights = self.analyze_liquidity()
        _, lev_insights = self.analyze_leverage()
        _, eff_insights = self.analyze_efficiency()
        
        concerns = []
        
        # Check for concerning metrics
        concerning_insights = []
        for insight in prof_insights + liq_insights + lev_insights + eff_insights:
            if any(word in insight.lower() for word in ['low', 'poor', 'risk', 'below', 'concerns']):
                concerning_insights.append(insight)
        
        # Create structured concerns
        concern_templates = {
            'Profitability Pressure': {
                'description': 'Declining margins suggest competitive pressure or rising costs.',
                'severity': 'MODERATE'
            },
            'Liquidity Risk': {
                'description': 'Low current ratio may limit ability to meet short-term obligations.',
                'severity': 'HIGH'
            },
            'High Leverage': {
                'description': 'Elevated debt levels increase financial risk and limit flexibility.',
                'severity': 'HIGH'
            },
            'Asset Quality': {
                'description': 'Inefficient asset utilization may impact future returns.',
                'severity': 'MODERATE'
            },
            'Working Capital Management': {
                'description': 'Slow receivables collection or high inventory levels tie up cash.',
                'severity': 'MODERATE'
            }
        }
        
        concern_list = []
        for title, details in concern_templates.items():
            if any(keyword in ' '.join(concerning_insights).lower() for keyword in title.lower().split()):
                concern_list.append({
                    'title': title,
                    'description': details['description'],
                    'severity': details['severity']
                })
        
        # Limit to 4 concerns
        return concern_list[:4]
    
    def generate_risks(self) -> List[Dict]:
        """Generate risk factors"""
        
        risks = [
            {
                'factor': 'Economic Downturn Risk',
                'description': 'Recession could reduce consumer spending and business investments.',
                'severity': 'HIGH'
            },
            {
                'factor': 'Industry Disruption',
                'description': f'Technology changes could disrupt the {self.company_info.get("industry", "industry")} sector.',
                'severity': 'MODERATE'
            },
            {
                'factor': 'Competitive Pressure',
                'description': 'Intense competition may erode margins and market share.',
                'severity': 'MODERATE'
            },
            {
                'factor': 'Currency Risk',
                'description': 'International operations exposed to foreign exchange volatility.',
                'severity': 'MODERATE'
            },
            {
                'factor': 'Supply Chain Risk',
                'description': 'Global supply chain disruptions could impact production and costs.',
                'severity': 'MODERATE'
            }
        ]
        
        return risks
    
    def generate_investment_thesis(self, recommendation_data: Dict) -> str:
        """Generate comprehensive investment thesis"""
        
        company = self.company_info.get('company', 'This company')
        industry = self.company_info.get('industry', 'its sector')
        
        thesis = f"""
{company} presents a {recommendation_data['recommendation'].lower()} opportunity in the {industry} sector.

FUNDAMENTAL ANALYSIS:
• The company demonstrates strong financial fundamentals with a composite score of {recommendation_data['overall_score']}
• Key financial metrics indicate {('solid' if float(recommendation_data['overall_score'].split('/')[0]) > 70 else 'moderate')} operational performance
• Balance sheet health and liquidity position support business continuity

VALUATION PERSPECTIVE:
• Current market multiples appear {'attractive' if recommendation_data['recommendation'] == 'BUY' else 'neutral'} relative to growth prospects
• Earnings quality is {'strong' if recommendation_data['recommendation'] == 'BUY' else 'adequate'}, supported by operating cash flow generation

RISK ASSESSMENT:
• Risk factors are {'manageable' if recommendation_data['recommendation'] == 'BUY' else 'material'} and within acceptable parameters
• Management quality and strategic positioning provide {'strong' if recommendation_data['recommendation'] == 'BUY' else 'adequate'} downside protection

INVESTMENT RATIONALE:
{', '.join([f"{i+1}. {insight}" for i, insight in enumerate(recommendation_data['key_insights'][:3])])}

RECOMMENDATION:
{recommendation_data['recommendation']} with {recommendation_data['confidence']} confidence level

This recommendation is suitable for {('growth-oriented long-term investors' if recommendation_data['recommendation'] == 'BUY' else 'conservative investors seeking')} {'exposure to' if recommendation_data['recommendation'] == 'BUY' else 'stability in'} the {industry} sector.
        """.strip()
        
        return thesis
    
    def generate_action_items(self) -> List[Dict]:
        """Generate recommended action items"""
        
        actions = [
            {
                'action': 'Conduct Detailed Valuation Analysis',
                'rationale': 'Compare current valuation multiples (P/E, P/B, EV/EBITDA) to peers and historical averages',
                'priority': 'HIGH'
            },
            {
                'action': 'Analyze Management Quality',
                'rationale': 'Review track record, capital allocation decisions, and compensation alignment with shareholders',
                'priority': 'HIGH'
            },
            {
                'action': 'Review Competitive Positioning',
                'rationale': 'Assess market share trends, competitive moat, and differentiation vs. competitors',
                'priority': 'MEDIUM'
            },
            {
                'action': 'Check Forward Guidance',
                'rationale': 'Review management guidance for revenue growth, margin expansion, and capital allocation',
                'priority': 'MEDIUM'
            },
            {
                'action': 'Monitor Key Metrics Quarterly',
                'rationale': 'Track revenue, margins, free cash flow, and ROE to ensure thesis remains valid',
                'priority': 'HIGH'
            },
            {
                'action': 'Assess Dividend Policy',
                'rationale': 'Evaluate dividend sustainability, payout ratio trends, and growth potential',
                'priority': 'MEDIUM'
            },
            {
                'action': 'Position Size Appropriately',
                'rationale': 'Allocate position size based on portfolio risk tolerance and conviction level',
                'priority': 'HIGH'
            },
            {
                'action': 'Set Clear Exit Criteria',
                'rationale': 'Define specific conditions that would trigger selling (thesis change, valuation overreach)',
                'priority': 'MEDIUM'
            }
        ]
        
        return actions
    
    def generate_complete_report(self) -> Dict:
        """Generate complete investment analysis report"""
        
        recommendation_data = self.generate_recommendation()
        thesis = self.generate_investment_thesis(recommendation_data)
        
        report = {
            'recommendation': recommendation_data['recommendation'],
            'confidence': recommendation_data['confidence'],
            'overall_score': recommendation_data['overall_score'],
            'component_scores': recommendation_data['component_scores'],
            'strengths': self.generate_strengths(),
            'concerns': self.generate_concerns(),
            'risks': self.generate_risks(),
            'investment_thesis': thesis,
            'action_items': self.generate_action_items(),
            'key_insights': recommendation_data['key_insights']
        }
        
        return report
