import unittest
from catalogo import listar_especialidades, buscar_especialidades

class TestCatalogo(unittest.TestCase):
    def test_hay_tres_especialidades(self):
        self.assertEqual(len(listar_especialidades()), 3)
    def test_busqueda_por_nombre(self):
        resultados = buscar_especialidades("software")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["nombre"], "Desarrollo de Software")
    def test_busqueda_sin_distinguir_mayusculas(self):
        resultados = buscar_especialidades("SISTEMAS")
        self.assertEqual(len(resultados), 1)
    def test_busqueda_sin_resultados(self):
        self.assertEqual(buscar_especialidades("astronomía"), [])
    def test_busqueda_vacia_devuelve_todo(self):
        self.assertEqual(len(buscar_especialidades(" ")), 3)

if __name__ == "__main__":
    unittest.main()