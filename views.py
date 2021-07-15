from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

data_of_users = [{
    "name": "Adam",
    "owes": {
        "Bob": 12.0,
        "Chuck": 4.0,
        "Dan": 9.5
    },
    "owed_by": {
        "Bob": 6.5,
        "Dan": 2.75
    },
    "balance": "",
},
    { "name": "Kevin",
    "owes": {
        "Bob": 12.0,
        "Chuck": 4.0,
        "Dan": 9.5
    },
    "owed_by": {
        "Bob": 6.5,
        "Dan": 2.75
    },
    "balance": "",
}
]


class UserResponse(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request):
        print(request)
        username = request.GET.get("name")
        content = {}
        for items in data_of_users.items():
            if items.get(username):
                content = {"name": username}
                return Response(content)
        return Response(content)

    def post(self, request):
        content = {"username": request.POST.get("username")}
        return Response(content)


class IOUResponse(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def post(self, request):
        for data in data_of_users:
            if request.POST.get("name") == data["name"]:
                for user in data.items():
                    total_owed_by = sum(user['owes'].values())
                    total_owed = sum(user['owes'].values())
                    data_of_users["balance"] = total_owed - total_owed_by
                return Response(data_of_users)
        return Response({})
