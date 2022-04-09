from django.test import TestCase
import datetime
from .models import Diary

# Create your tests here.

# TestCaseを必ず継承する

# 流れ　= モデルに直接テスト用の値を作成　＝＞　値を取得　＝＞　値がちゃんと入力されているか確かめる。比較etc...

class DiaryModelTests(TestCase):

    def test_diary_has_date(self):

        """
        作成した日記データに日付が付与されているか確認　 =>  テストで作って取って来て確かめる
        """
        # Diaryモデルに　.objects.create　で直接オブジェクトを指定した値で作成する。
        Diary.objects.create(title='test_title',text='test_text')
        # 今度は指定して作成した値を .objects.get で取り出してインスタンスを作成
        action_diary = Diary.objects.get(title='test_title')
        # 取り出したインスタンスの日付けが正しいか確かめる
        self.assertIsInstance(action_diary.date, datetime.date)
    

    def test_save_and_retrieve(self):

        """
        日記データの保存と取得を確認
        """
        # Diaryモデルに　.objects.create　で直接オブジェクトを指定した値で作成する。
        Diary.objects.create(title='test_title', text='test_text')
        # 度は指定して作成した値を .objects.get で取り出してインスタンスを作成
        actual_diary = Diary.objects.get(title='test_title')
        # 取り出したインスタンスのタイトルが指定した値と同じか比較している
        self.assertEqual(actual_diary.title, 'test_title')