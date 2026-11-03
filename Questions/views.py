from django.shortcuts import render, get_object_or_404
from Questions.models import Questions_Crud, AnswerSubmissionDB
from Questions.serializers import QuestionCRUDSerializer, AnswerSubmissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class QuestionCRUDListCreateView(APIView):
    def get(self, request):
        qs = Questions_Crud.objects.all()
        serializer_instance = QuestionCRUDSerializer(qs, many=True)
        return Response(serializer_instance.data)
    
    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionCRUDSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data 
            Questions_Crud.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        
        
class QuestionCRUDRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        # qs = Questions_Crud.objects.get(id=pk)
        qs = get_object_or_404(Questions_Crud, id=pk)
        serializer_instance = QuestionCRUDSerializer(qs)
        return Response(serializer_instance.data)
    
    def put(self, request, pk):
        form_data = request.data 
        serializer_instance = QuestionCRUDSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            Questions_Crud.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
    
    def delete(self, request, pk):
        Questions_Crud.objects.filter(id=pk).delete()
        return Response(data={"message":"Question deleted successfully."})

  
  
  
class AnswerSubmissionListCreateView(APIView):
    def get(self, request):
        qs = AnswerSubmissionDB.objects.all()
        serializer_instance = AnswerSubmissionSerializer(qs, many=True)
        return Response(serializer_instance.data)
    
    def post(self, request):
        form_data = request.data
        serializer_instance = AnswerSubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            AnswerSubmissionDB.objects.create(**actual_data)
            return Response(data = serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
        
class AnswerSubmissionRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        # qs = AnswerSubmissionDB.objects.get(id=pk)
        qs = get_object_or_404(AnswerSubmissionDB, id=pk)
        serializer_instance = AnswerSubmissionSerializer(qs)
        return Response(serializer_instance.data)
    
    def put(self, request, pk):
        form_data = request.data 
        serializer_instance = AnswerSubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            AnswerSubmissionDB.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
    
    def delete(self, request, pk):
        AnswerSubmissionDB.objects.filter(id=pk).delete()
        return Response(data={"message":"Answer deleted successfully."})

  
  
  
  