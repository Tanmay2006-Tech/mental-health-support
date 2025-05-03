class MoodDetector:
    """
    A simplified mood detection system that identifies emotions from text
    using keyword matching for both mood and context.
    """
    
    def __init__(self):
        # Define mood and context keywords
        self.mood_keywords = {
            'happy': ['happy', 'joy', 'excited', 'great', 'wonderful', 'good', 'glad', 'pleased'],
            'sad': ['sad', 'unhappy', 'depressed', 'down', 'blue', 'miserable'],
            'angry': ['angry', 'mad', 'annoyed', 'frustrated', 'irritated'],
            'neutral': []  # No keywords for neutral, used as a fallback
        }
        
        self.context_keywords = {
            'academic': ['exam', 'test', 'study', 'homework', 'assignment'],
            'work': ['job', 'work', 'boss', 'meeting', 'project'],
            'health': ['sick', 'ill', 'doctor', 'pain', 'hospital'],
            'relationship': ['friend', 'breakup', 'date', 'marriage', 'partner'],
            'neutral': []  # No keywords for neutral context
        }

    def detect_mood(self, user_input):
        """
        Detects the mood and context from the provided text input.
        
        Args:
            user_input (str): The text input from the user
            
        Returns:
            tuple: (mood, context) where:
                mood (str): The detected mood, or 'neutral' if none detected
                context (str): The detected context, or 'neutral' if none detected
        """
        user_input = user_input.lower()  # Convert the text to lowercase for matching
        
        # Initialize mood and context scores
        mood_scores = {mood: 0 for mood in self.mood_keywords}
        context_scores = {context: 0 for context in self.context_keywords}
        
        # Score mood
        for mood, keywords in self.mood_keywords.items():
            for keyword in keywords:
                if keyword in user_input:
                    mood_scores[mood] += 1
        
        # Score context
        for context, keywords in self.context_keywords.items():
            for keyword in keywords:
                if keyword in user_input:
                    context_scores[context] += 1
        
        # Detect the mood with the highest score
        detected_mood = max(mood_scores, key=mood_scores.get, default='neutral')
        
        # Detect the context with the highest score
        detected_context = max(context_scores, key=context_scores.get, default='neutral')
        
        return detected_mood, detected_context
