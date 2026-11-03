from rest_framework import serializers
from Questions.models import Questions_Crud, AnswerSubmissionDB

class QuestionCRUDSerializer(serializers.Serializer):
    
    question =serializers.CharField(max_length=500)
        
    option_a = serializers.CharField(max_length=200)
        
    option_b = serializers.CharField(max_length=200)
    
    option_c = serializers.CharField(max_length=200)

    option_d = serializers.CharField(max_length=200)
    
    correct_answer = serializers.CharField(max_length=500)
    

class AnswerSubmissionSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=200)
            
    question_id = serializers.IntegerField()
            
    selected_answer = serializers.CharField(max_length=200)
            
    submitted_at = serializers.DateTimeField(read_only = True)
    
    def validate(self, validated_data):
        question_id = validated_data.get("question_id")
        if not Questions_Crud.objects.filter(id = question_id).exists():
            raise serializers.ValidationError("Question does not exist...!")
        return validated_data