from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

@api_view(['GET', 'POST'])
def wheel_specifications_view(request):
    print("RECEIVED:", request.data)
    
    if request.method == 'POST':
        serializer = WheelSpecificationSerializer(data=request.data, many=False)
        if serializer.is_valid():
            spec = serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": spec.formNumber,
                    "submittedBy": spec.submittedBy,
                    "submittedDate": str(spec.submittedDate),
                    "status": spec.status
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        formNumber = request.GET.get("formNumber")
        submittedBy = request.GET.get("submittedBy")
        submittedDate = request.GET.get("submittedDate")

        queryset = WheelSpecification.objects.all()

        if formNumber:
            queryset = queryset.filter(formNumber=formNumber)
        if submittedBy:
            queryset = queryset.filter(submittedBy=submittedBy)
        if submittedDate:
            queryset = queryset.filter(submittedDate=submittedDate)

        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        })
