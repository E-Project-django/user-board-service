from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from boards.models import Freeboard, Notice, Staffboard
User = get_user_model()


class FreeboardViewSetTest(APITestCase):
    """ 자유게시판 Viewset action(list,create,retrieve,update,partial_update,destory)이 정상 작동하는지 확인하기 위한 테스트 """

    def setUp(self):
        self.user = User.objects.create_user(
            username='user', password='0000', age=25, gender='F', phone_number='010-1234-5678'
        )
        self.client.force_authenticate(self.user)
        self.freeboard = Freeboard.objects.create(
            title='자유게시판 제목 테스트 첫번째입니다.', content='자유게시판 본문 테스트 첫번째입니다.', author_id=self.user
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


class NoticeViewSetTest(APITestCase):
    """ 공지사항 Viewset action(list,create,retrieve,update,partial_update,destory)이 정상 작동하는지 확인하기 위한 테스트 """

    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff', password='0000', age=25, gender='F', phone_number='010-1234-5678', is_staff= True
        )
        self.client.force_authenticate(self.staff)
        self.notice = Notice.objects.create(
            title='공지사항 제목 테스트 첫번째입니다.', content='공지사항 본문 테스트 첫번째입니다.', author_id=self.staff
        )

    def test_user_create(self):
        data = {
            'title': '공지사항 제목 테스트 두번째입니다.',
            'content': '공지사항 본문 테스트 두번째입니다.',
            'author_id': 1
        }

        response = self.client.post(reverse('notice-list'), data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_user_get_list(self):
        response = self.client.get(reverse('notice-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_get_retrieve(self):
        response = self.client.get(reverse('notice-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        update_data = {
            'title': '공지사항 제목 수정중입니다.',
            'content': '공지사항 본문 수정중입니다.',
            'author_id': 1
        }
        response = self.client.put(reverse('notice-detail', kwargs={'pk': 1}), update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_partial_update(self):
        partial_update_data = {
            'content': '공지사항 본문 내용만 수정중입니다.',
        }
        response = self.client.patch(reverse('notice-detail', kwargs={'pk': 1}), partial_update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_destory(self):
        response = self.client.delete(reverse('notice-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class StaffboardViewSetTest(APITestCase):
    """ 운영자게시판 Viewset action(list,create,retrieve,update,partial_update,destory)이 정상 작동하는지 확인하기 위한 테스트 """

    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff', password='0000', age=25, gender='F', phone_number='010-1234-5678', is_staff=True
        )
        self.client.force_authenticate(self.staff)
        self.staffboard = Staffboard.objects.create(
            title='운영자 게시판 제목 테스트 첫번째입니다.', content='운영자 게시판 본문 테스트 첫번째입니다.', author_id=self.staff
        )

    def test_user_create(self):
        data = {
            'title': '운영자 게시판 제목 테스트 두번째입니다.',
            'content': '운영자 게시판 본문 테스트 두번째입니다.',
            'author_id': 1
        }

        response = self.client.post(reverse('staffboard-list'), data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_user_get_list(self):
        response = self.client.get(reverse('staffboard-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_get_retrieve(self):
        response = self.client.get(reverse('staffboard-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        update_data = {
            'title': '운영자 게시판 제목 수정중입니다.',
            'content': '운영자 게시판 본문 수정중입니다.',
            'author_id': 1
        }
        response = self.client.put(reverse('staffboard-detail', kwargs={'pk': 1}), update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_partial_update(self):
        partial_update_data = {
            'content': '운영자 게시판 본문 내용만 수정중입니다.',
        }
        response = self.client.patch(reverse('staffboard-detail', kwargs={'pk': 1}), partial_update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_destory(self):
        response = self.client.delete(reverse('staffboard-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
