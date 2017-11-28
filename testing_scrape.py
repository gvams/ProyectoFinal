import unittest
from scrape import get_total_records,current_target_url,get_json_data
from crud import selectFromBand,selectFromDiscography,selectFromMember, deleteFromMember,deleteFromDiscography,deleteFromBand,updateMemberName,updateDiscographyName,updateBandName

class test_scrape(unittest.TestCase):
    
    def test_current_target_url(self):
        self.assertEqual(current_target_url(1,0),'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&_=1505682951191')

    def test_selectFromBand(self):
        self.assertIsNone(selectFromBand('(Jhator)'),'Name:(Jhator),Id:,Country:Sweden,Location:Alingsås,Status:Active,Formed In:N/A,Years Active:N/A,Genre:Death n Roll,Lyrical Themes:N/A,Label:Unsigned/independent')

    def test_selectFromDiscography(self):
        self.assertNotEqual(selectFromDiscography('Checkpoint #4'),'Name: Checkpoint #3,Release Type: Split,Year: 2001')

    def test_selectFromMember(self):
        self.assertIsNone(selectFromMember('Joel Ekman'),'Band:12 Gauge Dead')

    def test_updateBandName(self):
        self.assertEqual(updateBandName('12 Gauge Dead','Twelve Gauge Dead'), None)

    def test_updateDiscographyName(self):
        self.assertIsNone(updateDiscographyName('Untitle','Untitled'))

    def test_updateMemberName(self):
        self.assertIsNone(updateMemberName('Kristoffer Matlak','Cristoffer Matlak'), None)

    def test_deleteFromBand(self):
        self.assertIsNone(deleteFromBand('2 ton Predator'))

    def test_deleteFromDiscography(self):
        self.assertIsNone(deleteFromDiscography('Untitled'))

    def test_deleteFromMember(self):
        self.assertIsNone(deleteFromMember('Maza'))    

   

if __name__ =='__main__':    
    unittest.main()
