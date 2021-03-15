DATASET_PATH = './data/dataset.xlsx'
TARGET_SEARCH_COLUMN_NAME = 'Name'

CLASS_NAME_1 = 'Albukerke'
CLASS_NAME_2 = 'Dum'
CLASS_NAME_3 = 'Baxan'

SEARCH_QUERY = '{N} == "{A}" | {N} == "{B}" | {N} == "{C}"'.format(
    N=TARGET_SEARCH_COLUMN_NAME, A=CLASS_NAME_1, B=CLASS_NAME_2, C=CLASS_NAME_3)

QUERY_CLASS_1 = '{N} == "{A}"'.format(
    N=TARGET_SEARCH_COLUMN_NAME, A=CLASS_NAME_1)
QUERY_CLASS_2 = '{N} == "{A}"'.format(
    N=TARGET_SEARCH_COLUMN_NAME, A=CLASS_NAME_2)
QUERY_CLASS_3 = '{N} == "{A}"'.format(
    N=TARGET_SEARCH_COLUMN_NAME, A=CLASS_NAME_3)

CRITERIA_1 = 'E (0-50)'
CRITERIA_2 = 'J (35-87)'
CRITERIA_3 = 'D (0-100)'

COLUMNS = [CRITERIA_1, CRITERIA_2, CRITERIA_3]
