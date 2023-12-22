from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        
        self.curso_1 = Curso.objects.create(
            codigo_curso="DV21", descricao="Curso DevOps teste", nivel="A"
        )

        self.curso_1 = Curso.objects.create(
            codigo_curso="QA22", descricao="Curso QA teste", nivel="I"
        )
    
    # def test_falhador(self):
    #     self.fail("O teste falhou de propósito, não se preocupe.")

    def test_request_get_list_cursos(self):
        """Teste para verificar a requisição GET para listar o cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_curso(self):
        """Teste para verificar a requisição POST para criar um cursos"""

        data = {
            "codigo_curso":"DV21", 
            "descricao":"Curso DevOps teste", 
            "nivel":"A"
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_curso(self):
        """Teste para verificar a requisição DELETE não permitida para um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put_update_curso(self):
        """Teste para verificar a requisição POST para criar um cursos"""

        data = {
            "codigo_curso":"DV21", 
            "descricao":"Curso DevOps teste atualizado", 
            "nivel":"B"
        }

        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)