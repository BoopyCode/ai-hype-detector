#!/usr/bin/env python3
# AI Hype Detector - Because not everything that glitters is AGI

import re
import sys
from datetime import datetime

class HypeDetector:
    def __init__(self):
        self.hype_words = [
            'revolutionary', 'game-changing', 'paradigm shift',
            'disruptive', 'magic', 'sentient', 'conscious',
            'AGI', 'superintelligence', 'singularity',
            'zero-shot', 'one-shot', 'no-code', 'auto-magic'
        ]
        self.buzzword_patterns = [
            r'\bAI\b.*\bsolution\b',  # "AI solution"
            r'\btransformative\b',
            r'\bnext-generation\b',
            r'\benterprise-grade\b.*\bAI\b'
        ]
    
    def analyze_text(self, text):
        """Returns hype score 0-100 where 100 = pure vaporware"""
        score = 0
        
        # Check for hype words
        for word in self.hype_words:
            if word.lower() in text.lower():
                score += 10
                print(f"🚨 Found hype word: '{word}' (+10)")
        
        # Check for buzzword patterns
        for pattern in self.buzzword_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                score += 15
                print(f"🎯 Buzzword pattern matched: '{pattern}' (+15)")
        
        # Check for unrealistic claims
        if re.search(r'\b100%\b.*\baccuracy\b', text, re.IGNORECASE):
            score += 25
            print(f"🤥 Found unrealistic claim: '100% accuracy' (+25)")
        
        if 'solve all your problems' in text.lower():
            score += 30
            print(f"💀 Found magical thinking: 'solve all your problems' (+30)")
        
        # Cap at 100
        return min(score, 100)
    
    def get_verdict(self, score):
        """Provide humorous but accurate assessment"""
        if score >= 80:
            return "🚨 MAXIMUM HYPE - Probably vaporware. Run away!"
        elif score >= 60:
            return "⚠️  HIGH HYPE - Strong buzzword energy. Tread carefully."
        elif score >= 40:
            return "🤔 MODERATE HYPE - Some substance, some fluff."
        elif score >= 20:
            return "👍 LOW HYPE - Might actually work. Still read the docs."
        else:
            return "✅ MINIMAL HYPE - Surprisingly reasonable. Still test it."

def main():
    print("\n🤖 AI HYPE DETECTOR 3000\n")
    print("Paste the AI tool/library description (Ctrl+D to finish):\n")
    
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        print("\n\nAborted by user")
        return
    
    if not text.strip():
        print("No text provided. Try: echo 'description' | python ai_hype_detector.py")
        return
    
    detector = HypeDetector()
    score = detector.analyze_text(text)
    
    print(f"\n📊 HYPE SCORE: {score}/100")
    print(f"\n🎯 VERDICT: {detector.get_verdict(score)}")
    
    if score > 50:
        print("\n💡 PRO TIP: Check if it has actual users, not just Medium articles")

if __name__ == "__main__":
    main()
