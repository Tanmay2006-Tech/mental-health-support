class MoodDetector:
    """
    A simple mood detection system that identifies emotions from text
    using keyword matching.
    """
    
    def __init__(self):
        
        self.mood_keywords = {
            'happy': ['happy', 'joy', 'excited', 'great', 'wonderful', 'good', 'glad', 'pleased',
                      'delighted', 'content', 'cheerful', 'thrilled', 'fantastic', 'excellent'],
                      
            'sad': ['sad', 'unhappy', 'depressed', 'down', 'blue', 'miserable', 'upset',
                    'disappointed', 'despair', 'grief', 'sorrow', 'gloomy', 'heartbroken'],
                    
            'anxious': ['anxious', 'worried', 'nervous', 'uneasy', 'afraid', 'fear', 'scared',
                        'frightened', 'panic', 'stress', 'tense', 'concerned', 'apprehensive',
                        'exam', 'test', 'presentation', 'interview', 'deadline'],
                        
            'angry': ['angry', 'mad', 'annoyed', 'frustrated', 'irritated', 'furious', 'rage',
                      'outraged', 'hostile', 'bitter', 'resentful', 'upset', 'irate'],
                      
            'stressed': ['stressed', 'overwhelmed', 'pressure', 'burden', 'strain', 'tension',
                         'exhausted', 'tired', 'drained', 'burnt out', 'overworked', 'busy',
                         'deadline', 'too much', 'assignment', 'project', 'exam', 'test', 'study',
                         'homework', 'tomorrow', 'due']
        }
        
        
        self.context_keywords = {
            'academic': ['exam', 'test', 'quiz', 'study', 'homework', 'assignment', 'project', 
                         'paper', 'essay', 'class', 'course', 'school', 'college', 'university', 
                         'grade', 'professor', 'teacher', 'lecture', 'semester', 'final'],
            'work': ['job', 'work', 'boss', 'meeting', 'project', 'deadline', 'presentation', 
                    'client', 'report', 'interview', 'promotion', 'career', 'office', 'colleague'],
            'health': ['sick', 'ill', 'doctor', 'pain', 'hurt', 'hospital', 'health', 'disease', 
                      'symptom', 'medication', 'medicine', 'treatment', 'diagnosis', 'recovery'],
            'relationship': ['friend', 'breakup', 'date', 'relationship', 'marriage', 'divorce', 
                            'partner', 'girlfriend', 'boyfriend', 'spouse', 'family', 'parent']
        }
        

        self.default_mood = 'neutral'
    
    def detect_mood(self, text):
        """
        Detects the mood from the provided text
        
        Args:
            text (str): The text input from the user
            
        Returns:
            tuple: (mood, context) where:
                mood: str - the detected mood, or 'neutral' if none detected
                context: str - the detected context or None if none detected
        """
        text = text.lower()
        
        
        mood_scores = {}
        for mood, keywords in self.mood_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in text.split() or f" {keyword} " in f" {text} ":
                    score += 1
            if score > 0:
                mood_scores[mood] = score
        
        
        context_scores = {}
        for context, keywords in self.context_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in text.split() or f" {keyword} " in f" {text} ":
                    score += 1
            if score > 0:
                context_scores[context] = score
        
        
        detected_mood = self.default_mood
        if mood_scores:
            detected_mood = max(mood_scores, key=mood_scores.get)
        
        
        detected_context = None
        if context_scores:
            detected_context = max(context_scores, key=context_scores.get)
            
        return detected_mood, detected_context
