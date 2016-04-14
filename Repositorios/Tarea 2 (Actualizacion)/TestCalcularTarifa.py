'''
Created on Apr 21, 2015

@author: Francisco Javier
         Arleyn Goncalves
'''
import unittest
import datetime
import CalculaTarifas


class Test(unittest.TestCase):

    def testCalcularPrecios(self):
        pass
    
    def testTarifaNula(self):
        tarifa = CalculaTarifas.Tarifa(0,0);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,27,0,0,0)];
        self.assertEqual(0,CalculaTarifas.calcularPrecio(tarifa,tiempo))
    
    # Prueba Frontera lo minimo son 15 dias en un dia de semana
    
    def test15MinutosSemana(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,21,16,15,0)];
        
        self.assertEqual(5,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba Frontera lo minimo son 15 dias en un fin de semana
        
    def test15MinutosFinSemana(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,25,16,0,0),
                                    datetime.datetime(2015,4,25,16,15,0)];
        
        self.assertEqual(10,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba 5 dias exacto de Lunes a Viernes
        
    def test5DiasSemanaExacto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,25,0,0,0)];
        
        self.assertEqual(600,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba 2 dias exactos de Sabado a Domingo
        
    def test2DiasFinSemanaExacto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,25,0,0,0),
                                    datetime.datetime(2015,4,27,0,0,0)];
        
        self.assertEqual(480,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba de 1 hora y 1 minuto, probar que se cobra 2 horas

    def test1hora1minuto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,21,17,1,0)];
        
        self.assertEqual(10,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba de 1 hora exacta
        
    def test1horaexacta(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,21,17,0,0)];
        
        self.assertEqual(5,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba de 23 horas 

    def test23horasexacta(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,22,15,0,0)];
        
        self.assertEqual(115,CalculaTarifas.calcularPrecio(tarifa,tiempo))        
        
    # Prueba de 1 dia exacto
        
    def test1diaexacto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,22,16,0,0)];
        
        self.assertEqual(120,CalculaTarifas.calcularPrecio(tarifa,tiempo))   
        
    # Prueba de Limite Frontera 7 dias Exactos
        
    def test7dias(self):
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,28,16,0,0)];
        
        self.assertEqual(1080,CalculaTarifas.calcularPrecio(tarifa,tiempo)) 
        
    # Test Menos de 15 min
        
    def testMenos15Min(self):
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,21,14,59,0)];
        self.assertRaises(Exception,lambda: CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Test Mas de 7 dias
    
    def testMas7Dias(self):
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,28,0,1,0)];
        self.assertRaises(Exception,lambda: CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Test tarifa Negativa
    
    def testTarifaNegativa(self):
        tarifa = CalculaTarifas.Tarifa(-5,-10);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,28,0,1,0)];
        self.assertRaises(Exception,lambda: CalculaTarifas.calcularPrecio(tarifa,tiempo))

    # Fin de reservacion mayor a inicio de reservacion
    
    def testFechas(self):
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,19,0,0,0)];
        self.assertRaises(Exception,lambda: CalculaTarifas.calcularPrecio(tarifa,tiempo)) 
        
    # Las tarifas son decimales
    
    def testTarifaDecimal(self):
        tarifa = CalculaTarifas.Tarifa(0.5,2);
        tiempo = [datetime.datetime(2015,4,21,0,0,0),
                                    datetime.datetime(2015,4,21,1,15,0)];
        self.assertEqual(1,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()