from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from boards.models import Freeboard
User = get_user_model()


class FreeboardViewSetTest(APITestCase):
    """ 자유게시판 Viewset action(list,create,retrieve,update,partial_update,destory)이 정상 작동하는지 확인하기 위한 테스트 """

    def setUp(self):
        self.user = User.objects.create_user(
            username='user', password='0000', age=25, gender='F', phone_number='010-1234-5678'
        )
        self.client.login(username='user', password='0000')
        self.freeboard = Freeboard.objects.create(
            title='자유게시판 제목 테스트 첫번째입니다.', content='자유게시판 본문 테스트 두번째입니다.', author_id=self.user
        )

    def test_user_create(self):
        data = {
            'title': '자유게시판 제목 테스트 두번째입니다.',
            'content': '자유게시판 본문 테스트 두번째입니다.',
            'author_id': 1
        }

        response = self.client.post(reverse('freeboard-list'), data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_user_get_list(self):
        response = self.client.get(reverse('freeboard-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_get_retrieve(self):
        response = self.client.get(reverse('freeboard-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        update_data = {
            'title': '자유게시판 제목 수정중입니다.',
            'content': '자유게시판 본문 수정중입니다.',
            'author_id': 1
        }
        response = self.client.put(reverse('freeboard-detail', kwargs={'pk': 1}), update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_partial_update(self):
        partial_update_data = {
            'content': '자유게시판 본문 내용만 수정중입니다.',
        }
        response = self.client.patch(reverse('freeboard-detail', kwargs={'pk': 1}), partial_update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_destory(self):
        response = self.client.delete(reverse('freeboard-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
