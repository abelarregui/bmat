import unittest
from data_sources.csv_source import CsvSourceType1

# References: https://realpython.com/python-testing/

class TestCsvSourceType1(unittest.TestCase):

    def test_transform_to_list_dict(self):
        """
        Integration test for checking transformation function.
        """
        path_csv = r'data/db_works_test.csv'
        csv_data = CsvSourceType1(path_csv)
        output_expected = [
            {'_id': 91695, 'iswc': 'T0350190010', 'titles': [{'title': 'AL PIE DE MI TUMBA', 'type': 'OriginalTitle'}],
             'right_owners': [{'name': 'VICTOR CORDERO AURRECOECHEA', 'role': 'Compositor/Autor', 'ipi': '00006771296'},
                              {'name': 'EDIT MEX DE MUSICA INT S A', 'role': 'Editor', 'ipi': '00159586128'}]},
            {'_id': 606989, 'iswc': 'T0421424954', 'titles': [{'title': 'CANCION DEL MOLINO', 'type': 'OriginalTitle'}],
             'right_owners': [{'name': 'A K M (AUSTRIA)', 'role': 'Compositor', 'ipi': ''},
                              {'name': 'MANUEL LOPEZ QUIROGA MIQUEL', 'role': 'Compositor', 'ipi': '00018483968'},
                              {'name': 'SALVADOR VALVERDE LOPEZ', 'role': 'Compositor/Autor', 'ipi': '00089546523'},
                              {'name': 'RAFAEL DE LEON ARIAS DE SAAVEDRA', 'role': 'Autor', 'ipi': '00017821298'},
                              {'name': 'ANDRE BADET DE', 'role': 'Autor', 'ipi': '00001780714'}]},
            {'_id': 611321, 'iswc': 'T0421644792',
             'titles': [{'title': 'CHA CHA CHA DE BAHIA', 'type': 'OriginalTitle'},
                        {'title': 'CHA CHACHA EN BAHIA', 'type': 'AlternativeTitle'},
                        {'title': 'CHA CHACHA EN BAHÍA', 'type': 'AlternativeTitle'},
                        {'title': 'CHACHACHA EN BAHIA', 'type': 'AlternativeTitle'}], 'right_owners': [
                {'name': 'ENRIQUE JESUS JORRIN Y OLEAGA', 'role': 'Compositor/Autor', 'ipi': '00015546498'},
                {'name': 'EDMOND DAVID BACRI', 'role': 'Adaptador', 'ipi': '00001772516'}]},
            {'_id': 2141219, 'iswc': 'T0420889173', 'titles': [{'title': 'MALA YERBA', 'type': 'OriginalTitle'}],
             'right_owners': [{'name': 'RAFAEL MENDIZABAL ITURAIN', 'role': 'Autor', 'ipi': '00200703727'},
                              {'name': 'JOSE CARPENA SORIANO', 'role': 'Autor', 'ipi': '00222061816'},
                              {'name': 'FRANCISCO MARTINEZ SOCIAS', 'role': 'Compositor', 'ipi': '00222084113'}]},
            {'_id': 2595145, 'iswc': 'T0426508306', 'titles': [{'title': 'BATIRI RCA', 'type': 'OriginalTitle'},
                                                               {'title': 'BATIRI', 'type': 'AlternativeTitle'}],
             'right_owners': [{'name': 'MAXIMILIANO MORE BARTOLOME', 'role': 'Compositor/Autor', 'ipi': '00068238360'},
                              {'name': 'EDIT MEX DE MUSICA INT S A', 'role': 'Editor', 'ipi': '00159586128'}]}]
        self.assertEqual(csv_data.transform_to_list_dict(), output_expected, f"Should be {output_expected}")


if __name__ == '__main__':
    unittest.main()
