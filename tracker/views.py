from rest_framework import viewsets
from rest_framework.response import Response
from .models import JobApplication
from .serializers import JobApplicationSerializer
from .matcher import calculate_match
from django.shortcuts import render


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        result = calculate_match(
            self.request.data.get('my_skills', ''),
            self.request.data.get('job_description', '')
        )
        serializer.save(
            match_score=result['score'],
            missing_skills=', '.join(result['missing_skills'])
        )

    def perform_update(self, serializer):
        result = calculate_match(
            self.request.data.get('my_skills', ''),
            self.request.data.get('job_description', '')
        )
        serializer.save(
            match_score=result['score'],
            missing_skills=', '.join(result['missing_skills'])
        )


def home_page(request):
    applications = JobApplication.objects.all().order_by('-applied_date')
    return render(request, 'tracker/home.html', {'applications': applications})