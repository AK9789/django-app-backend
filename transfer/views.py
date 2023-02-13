from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication # get user
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .models import History
from .serializer import HistorySerializer

class Transfer(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        """
        sender = request.user
        recever = User.objects.filter(account_number__exact=pk)
        recever_details = User.objects.filter(account_number__exact=pk).values()
        recever_more = User.objects.filter(account_number__exact=pk).values_list('balance',flat=True)
        
        # me = User.objects.get(username=recever)
        # print(request.user)
        print(request.data.get("amount"))
        # print(pk)

        print(sender.balance)
        print('-------------------------------')
        print(recever)
        print(recever_details)
        # print(me)
        print(list(recever_more)[0])
        """


        """
        sender = request.user
        recever = User.objects.filter(account_number__exact=pk).values_list('balance',flat=True)
        amount = int(request.data.get("amount"))
        
        sender_balance = sender.balance
        recever_balance = list(recever)[0]

        print(type(recever_balance))
        print(type(sender_balance))
        print(type(amount))

        print(recever_balance)
        print(sender_balance)
        print(amount)
        
        if(amount <= sender_balance):
            print(amount)
            
        else:
            return Response({'msg': 'Not enough balance'}, status=status.HTTP_400_BAD_REQUEST)

        """
    

        recever_id = list(User.objects.filter(account_number__exact=pk).values_list('id',flat=True))[0]
        recever_balance = list(User.objects.filter(account_number__exact=pk).values_list('balance',flat=True))[0]
        recever_username = list(User.objects.filter(account_number__exact=pk).values_list('username',flat=True))[0]
        print(recever_username)
        # recever = User.objects.filter(account_number__exact=pk)
        recever = User.objects.get(username__iexact=recever_username)
        sender_id = request.user.id
        sender_balance = request.user.balance
        sender_username = request.user.username
        sender = request.user
        amount = int(request.data.get("amount"))


        # print(f'recever id {recever_id} type: {type(recever_id)}| username {recever_username} | balance {recever_balance} type: {type(recever_balance)} ')
        # print(f'sender id {sender_id} type: {type(sender_id)}| username {sender_username} | balance {sender_balance} type: {type(sender_balance)} ')
        # print(f'amount {amount} type: {type(amount)}')
        # print('/////////////////////////////////////////////')
        # print(sender)
        # print(recever)

        if(amount <= sender_balance):
            # sender amount
            amt_s = sender_balance - amount
            User.objects.filter(pk=sender_id).update(balance=amt_s)
            sender_history = History(
                attach=sender,
                name=recever_username,
                amount=amount,
                sent_type=False
            )
            sender_history.save()
            # print(f'sender balance: {amt_s}')

            # recever amount
            amt_r = recever_balance + amount
            User.objects.filter(pk=recever_id).update(balance=amt_r)
            recever_history = History(
                attach=recever,
                name=sender_username,
                amount=amount,
                sent_type=True
            )
            recever_history.save()
      

            # print(f'recever balance: {amt_r}')
            return Response({
                "success": True
            })

        else:
            return Response({'msg': 'Not enough balance'}, status=status.HTTP_400_BAD_REQUEST)



class HistoryList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        history_list = History.objects.filter(attach__exact=request.user.id).order_by('-time')
        serializer = HistorySerializer(history_list, many=True)

        return Response({
            "data": serializer.data
        })
