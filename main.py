from src.masks import get_mask_account, get_mask_card_number
from src.utils import json_to_dict

if __name__ == '__main__':
    print(get_mask_account(35383033474447895560))
    print(get_mask_card_number(1234567890123456))


if __name__ == '__main__':
    print(json_to_dict('operations.json'))