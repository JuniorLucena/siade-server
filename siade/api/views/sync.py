from django.core.exceptions import ValidationError
from rest_framework import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class SyncView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.filter_queryset(self.get_queryset()),
            data=request.DATA,
            many=True
        )
        if serializer.is_valid():
            try:
                [self.pre_save(obj) for obj in serializer.object]
            except ValidationError as err:
                # full_clean on model instances may be called in pre_save
                # so we have to handle eventual errors.
                return Response(err.message_dict,
                                status=status.HTTP_400_BAD_REQUEST)
            self.object = serializer.save()
            [self.post_save(obj, created=False) for obj in self.object]
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
