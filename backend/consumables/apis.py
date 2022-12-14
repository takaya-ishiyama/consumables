from .models import Items                          # モデル呼出
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView   # API
from .serializers import ItemSerializer                # APIで渡すデータをJSON,XML変換

class api(ListCreateAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = Items.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = ItemSerializer

    # 認証
    permission_classes = []