# -*- coding: utf-8 -*-
from random import randint
from PIL import Image, ImageDraw
from .dados import Gerador

def run():
	img = Image.new('RGB', (200, 180), 'white')
	dw = ImageDraw.Draw(img)
	gen = Gerador()

	def draw_quadra(numero, lados, pontos=None):
		dw.rectangle(pontos, fill=0)
		return Gerador.gerar_quadra(gen, numero, lados, pontos)

	gen.gerar_quadra = draw_quadra
	quadras = gen.gerar_quadras(randint(4, 8), randint(4, 8))
	img.save('bairro.png')