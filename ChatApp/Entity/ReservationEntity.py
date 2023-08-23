class ReservationEntity:
    """申請情報を保持するEntityクラス"""

    def __init__(self, id, message, status):
        """コンストラクタ
        
        Args:
        * id (String): 予約ID
        * message (String):申請状況についてのメッセージ
        * status (String): 申請状況
        """

        self.id = id
        self.message = message
        self.status = status