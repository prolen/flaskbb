# -*- coding: utf-8 -*-
"""change emoji shortcodes to characters

Revision ID: 232e68a03aa2
Revises: af3f5579c84d
Create Date: 2018-02-28 21:31:35.260704

"""
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232e68a03aa2'
down_revision = 'af3f5579c84d'
branch_labels = ()
depends_on = None


_emoji_replacement_mapping = {
    # bowtie:               not in Unicode
    # neckbeard:            not in Unicode
    # shipit, squirrel:     GitHub inside joke? either way, not in Unicode
    # trollface:            ancient meme, not in Unicode
    # octocat:              that's a brand logo, of course it's not in Unicode
    # flaskbb:              that's our logo! sadly not in Unicode though
    # feelsgood:            doom reference, not in Unicode
    # finnadie:             doom reference, not in Unicode
    # goberserk:            doom reference, not in Unicode
    # godmode:              doom reference, not in Unicode
    # hurtrealbad:          doom reference, not in Unicode
    # rage1:                doom reference, not in Unicode
    # rage2:                doom reference, not in Unicode
    # rage3:                doom reference, not in Unicode
    # rage4:                doom reference, not in Unicode
    # suspect:              doom reference, not in Unicode
    '+1': '👍',
    '-1': '👎',
    '100': '💯',
    '1234': '🔢',
    '8ball': '🎱',
    'a': '🅰️',
    'ab': '🆎',
    'abc': '🔤',
    'abcd': '🔡',
    'accept': '🉑',
    'aerial_tramway': '🚡',
    'airplane': '✈️',
    'alarm_clock': '⏰',
    'alien': '👽',
    'ambulance': '🚑',
    'anchor': '⚓️',
    'angel': '👼',
    'anger': '💢',
    'angry': '😠',
    'anguished': '😧',
    'ant': '🐜',
    'apple': '🍎',
    'aquarius': '♒️',
    'aries': '♈️',
    'arrow_backward': '◀️',
    'arrow_double_down': '⏬',
    'arrow_double_up': '⏫',
    'arrow_down': '⬇️',
    'arrow_down_small': '🔽',
    'arrow_forward': '▶️',
    'arrow_heading_down': '⤵️',
    'arrow_heading_up': '⤴️',
    'arrow_left': '⬅️',
    'arrow_lower_left': '↙️',
    'arrow_lower_right': '↘️',
    'arrow_right': '➡️',
    'arrow_right_hook': '↪️',
    'arrow_up': '⬆️',
    'arrow_up_down': '↕️',
    'arrow_up_small': '🔼',
    'arrow_upper_left': '↖️',
    'arrow_upper_right': '↗️',
    'arrows_clockwise': '🔃',
    'arrows_counterclockwise': '🔄',
    'art': '🎨',
    'articulated_lorry': '🚛',
    'astonished': '😲',
    'atm': '🏧',
    'b': '🅱️',
    'baby': '👶',
    'baby_bottle': '🍼',
    'baby_chick': '🐤',
    'baby_symbol': '🚼',
    'back': '🔙',
    'baggage_claim': '🛄',
    'balloon': '🎈',
    'ballot_box_with_check': '☑️',
    'bamboo': '🎍',
    'banana': '🍌',
    'bangbang': '‼️',
    'bank': '🏦',
    'bar_chart': '📊',
    'barber': '💈',
    'baseball': '⚾️',
    'basketball': '🏀',
    'bath': '🛀',
    'bathtub': '🛁',
    'battery': '🔋',
    'bear': '🐻',
    'bee': '🐝',
    'beer': '🍺',
    'beers': '🍻',
    'beetle': '🐞',
    'beginner': '🔰',
    'bell': '🔔',
    'bento': '🍱',
    'bicyclist': '🚴',
    'bike': '🚲',
    'bikini': '👙',
    'bird': '🐦',
    'birthday': '🎂',
    'black_circle': '⚫️',
    'black_joker': '🃏',
    'black_medium_small_square': '◾️',
    'black_medium_square': '◼️',
    'black_nib': '✒️',
    'black_small_square': '▪️',
    'black_square': '⬛',  # i assume that's black large square
    'black_square_button': '🔲',
    'blossom': '🌼',
    'blowfish': '🐡',
    'blue_book': '📘',
    'blue_car': '🚙',
    'blue_heart': '💙',
    'blush': '😊',
    'boar': '🐗',
    'boat': '⛵️',
    'bomb': '💣',
    'book': '📖',
    'bookmark': '🔖',
    'bookmark_tabs': '📑',
    'books': '📚',
    'boom': '💥',
    'boot': '👢',
    'bouquet': '💐',
    'bow': '🙇',
    'bowling': '🎳',
    'boy': '👦',
    'bread': '🍞',
    'bride_with_veil': '👰',
    'bridge_at_night': '🌉',
    'briefcase': '💼',
    'broken_heart': '💔',
    'bug': '🐛',
    'bulb': '💡',
    'bullettrain_front': '🚅',
    'bullettrain_side': '🚄',
    'bus': '🚌',
    'busstop': '🚏',
    'bust_in_silhouette': '👤',
    'busts_in_silhouette': '👥',
    'cactus': '🌵',
    'cake': '🍰',
    'calendar': '📆',
    'calling': '📲',
    'camel': '🐫',
    'camera': '📷',
    'cancer': '♋️',
    'candy': '🍬',
    'capital_abcd': '🔠',
    'capricorn': '♑️',
    'car': '🚗',
    'card_index': '📇',
    'carousel_horse': '🎠',
    'cat': '🐱',
    'cat2': '🐈',
    'cd': '💿',
    'chart': '💹',
    'chart_with_downwards_trend': '📉',
    'chart_with_upwards_trend': '📈',
    'checkered_flag': '🏁',
    'cherries': '🍒',
    'cherry_blossom': '🌸',
    'chestnut': '🌰',
    'chicken': '🐔',
    'children_crossing': '🚸',
    'chocolate_bar': '🍫',
    'christmas_tree': '🎄',
    'church': '⛪️',
    'cinema': '🎦',
    'circus_tent': '🎪',
    'city_sunrise': '🌇',
    'city_sunset': '🌆',
    'cl': '🆑',
    'clap': '👏',
    'clapper': '🎬',
    'clipboard': '📋',
    'clock1': '🕐',
    'clock10': '🕙',
    'clock1030': '🕥',
    'clock11': '🕚',
    'clock1130': '🕦',
    'clock12': '🕛',
    'clock1230': '🕧',
    'clock130': '🕜',
    'clock2': '🕑',
    'clock230': '🕝',
    'clock3': '🕒',
    'clock330': '🕞',
    'clock4': '🕓',
    'clock430': '🕟',
    'clock5': '🕔',
    'clock530': '🕠',
    'clock6': '🕕',
    'clock630': '🕡',
    'clock7': '🕖',
    'clock730': '🕢',
    'clock8': '🕗',
    'clock830': '🕣',
    'clock9': '🕘',
    'clock930': '🕤',
    'closed_book': '📕',
    'closed_lock_with_key': '🔐',
    'closed_umbrella': '🌂',
    'cloud': '☁️',
    'clubs': '♣️',
    'cn': '🇨🇳',
    'cocktail': '🍸',
    'coffee': '☕️',
    'cold_sweat': '😰',
    'collision': '💥',
    'computer': '💻',
    'confetti_ball': '🎊',
    'confounded': '😖',
    'confused': '😕',
    'congratulations': '㊗',
    'construction': '🚧',
    'construction_worker': '👷',
    'convenience_store': '🏪',
    'cookie': '🍪',
    'cool': '🆒',
    'cop': '👮',
    'copyright': '©️',
    'corn': '🌽',
    'couple': '👫',
    'couple_with_heart': '💑',
    'couplekiss': '💏',  # kiss
    'cow': '🐮',
    'cow2': '🐄',
    'credit_card': '💳',
    'crescent_moon': '🌙',
    'crocodile': '🐊',
    'crossed_flags': '🎌',
    'crown': '👑',
    'cry': '😢',
    'crying_cat_face': '😿',
    'crystal_ball': '🔮',
    'cupid': '💘',
    'curly_loop': '➰',
    'currency_exchange': '💱',
    'curry': '🍛',
    'custard': '🍮',
    'customs': '🛃',
    'cyclone': '🌀',
    'dancer': '💃',
    'dancers': '👯',
    'dango': '🍡',
    'dart': '🎯',
    'dash': '💨',
    'date': '📅',
    'de': '🇩🇪',
    'deciduous_tree': '🌳',
    'department_store': '🏬',
    'diamond_shape_with_a_dot_inside': '💠',
    'diamonds': '♦️',
    'disappointed': '😞',
    'disappointed_relieved': '😥',
    'dizzy': '💫',
    'dizzy_face': '😵',
    'do_not_litter': '🚯',
    'dog': '🐶',
    'dog2': '🐕',
    'dollar': '💵',
    'dolls': '🎎',
    'dolphin': '🐬',
    'donut': '🍩',  # it's doughnut, you 'muricans
    'door': '🚪',
    'doughnut': '🍩',
    'dragon': '🐉',
    'dragon_face': '🐲',
    'dress': '👗',
    'dromedary_camel': '🐪',
    'droplet': '💧',
    'dvd': '📀',
    'e-mail': '📧',
    'ear': '👂',
    'ear_of_rice': '🌾',
    'earth_africa': '🌍',
    'earth_americas': '🌎',
    'earth_asia': '🌏',
    'egg': '🥚',
    'eggplant': '🍆',
    'eight': '8️⃣',
    'eight_pointed_black_star': '✴️',
    'eight_spoked_asterisk': '✳️',
    'electric_plug': '🔌',
    'elephant': '🐘',
    'email': '✉️',
    'end': '🔚',
    'envelope': '✉️',
    'es': '🇪🇸',
    'euro': '💶',
    'european_castle': '🏰',
    'european_post_office': '🏤',
    'evergreen_tree': '🌲',
    'exclamation': '❗️',
    'expressionless': '😑',
    'eyeglasses': '👓',
    'eyes': '👀',
    'facepunch': '👊',
    'factory': '🏭',
    'fallen_leaf': '🍂',
    'family': '👪',
    'fast_forward': '⏩',
    'fax': '📠',
    'fearful': '😨',
    'feet': '🐾',
    'ferris_wheel': '🎡',
    'file_folder': '📁',
    'fire': '🔥',
    'fire_engine': '🚒',
    'fireworks': '🎆',
    'first_quarter_moon': '🌓',
    'first_quarter_moon_with_face': '🌛',
    'fish': '🐟',
    'fish_cake': '🍥',
    'fishing_pole_and_fish': '🎣',
    'fist': '✊',
    'five': '5️⃣',
    'flags': '🎏',
    'flashlight': '🔦',
    'floppy_disk': '💾',
    'flower_playing_cards': '🎴',
    'flushed': '😳',
    'foggy': '🌁',
    'football': '🏈',
    'fork_and_knife': '🍴',
    'fountain': '⛲️',
    'four': '4️⃣',
    'four_leaf_clover': '🍀',
    'fr': '🇫🇷',
    'free': '🆓',
    'fried_shrimp': '🍤',
    'fries': '🍟',
    'frog': '🐸',
    'frowning': '😦',
    'fu': '🖕',
    'fuelpump': '⛽️',
    'full_moon': '🌕',
    'full_moon_with_face': '🌝',
    'game_die': '🎲',
    'gb': '🇬🇧',
    'gem': '💎',
    'gemini': '♊️',
    'ghost': '👻',
    'gift': '🎁',
    'gift_heart': '💝',
    'girl': '👧',
    'globe_with_meridians': '🌐',
    'goat': '🐐',
    'golf': '⛳️',
    'grapes': '🍇',
    'green_apple': '🍏',
    'green_book': '📗',
    'green_heart': '💚',
    'grey_exclamation': '❕',
    'grey_question': '❔',
    'grimacing': '😬',
    'grin': '😁',
    'grinning': '😀',
    'guardsman': '💂',
    'guitar': '🎸',
    'gun': '🔫',
    'haircut': '💇',
    'hamburger': '🍔',
    'hammer': '🔨',
    'hamster': '🐹',
    'hand': '✋',
    'handbag': '👜',
    'hankey': '💩',
    'hash': '#️⃣',
    'hatched_chick': '🐥',
    'hatching_chick': '🐣',
    'headphones': '🎧',
    'hear_no_evil': '🙉',
    'heart': '❤️',
    'heart_decoration': '💟',
    'heart_eyes': '😍',
    'heart_eyes_cat': '😻',
    'heartbeat': '💓',
    'heartpulse': '💗',
    'hearts': '♥️',
    'heavy_check_mark': '✔️',
    'heavy_division_sign': '➗',
    'heavy_dollar_sign': '💲',
    'heavy_exclamation_mark': '❗️',
    'heavy_minus_sign': '➖',
    'heavy_multiplication_x': '✖️',
    'heavy_plus_sign': '➕',
    'helicopter': '🚁',
    'herb': '🌿',
    'hibiscus': '🌺',
    'high_brightness': '🔆',
    'high_heel': '👠',
    'hocho': '🔪',
    'honey_pot': '🍯',
    'honeybee': '🐝',
    'horse': '🐴',
    'horse_racing': '🏇',
    'hospital': '🏥',
    'hotel': '🏨',
    'hotsprings': '♨️',
    'hourglass': '⌛️',
    'hourglass_flowing_sand': '⏳',
    'house': '🏠',
    'house_with_garden': '🏡',
    'hushed': '😯',
    'ice_cream': '🍨',
    'icecream': '🍦',
    'id': '🆔',
    'ideograph_advantage': '🉐',
    'imp': '👿',
    'inbox_tray': '📥',
    'incoming_envelope': '📨',
    'information_desk_person': '💁',
    'information_source': 'ℹ️',
    'innocent': '😇',
    'interrobang': '⁉️',
    'iphone': '📱',
    'it': '🇮🇹',
    'izakaya_lantern': '🏮',
    'jack_o_lantern': '🎃',
    'japan': '🗾',
    'japanese_castle': '🏯',
    'japanese_goblin': '👺',
    'japanese_ogre': '👹',
    'jeans': '👖',
    'joy': '😂',
    'joy_cat': '😹',
    'jp': '🇯🇵',
    'key': '🔑',
    'keycap_ten': '🔟',
    'kimono': '👘',
    'kiss': '💋',
    'kissing': '😗',
    'kissing_cat': '😽',
    'kissing_closed_eyes': '😚',
    'kissing_face': '😗',  # aparently, the shortcode is just 'kissing'
    'kissing_heart': '😘',
    'kissing_smiling_eyes': '😙',
    'koala': '🐨',
    'koko': '🈁',
    'kr': '🇰🇷',
    'large_blue_circle': '🔵',
    'large_blue_diamond': '🔷',
    'large_orange_diamond': '🔶',
    'last_quarter_moon': '🌗',
    'last_quarter_moon_with_face': '🌜',
    'laughing': '😆',
    'leaves': '🍃',
    'ledger': '📒',
    'left_luggage': '🛅',
    'left_right_arrow': '↔️',
    'leftwards_arrow_with_hook': '↩️',
    'lemon': '🍋',
    'leo': '♌️',
    'leopard': '🐆',
    'libra': '♎️',
    'light_rail': '🚈',
    'link': '🔗',
    'lips': '👄',
    'lipstick': '💄',
    'lock': '🔒',
    'lock_with_ink_pen': '🔏',
    'lollipop': '🍭',
    'loop': '➿',
    'loudspeaker': '📢',
    'love_hotel': '🏩',
    'love_letter': '💌',
    'low_brightness': '🔅',
    'm': 'Ⓜ️',
    'mag': '🔍',
    'mag_right': '🔎',
    'mahjong': '🀄️',
    'mailbox': '📫',
    'mailbox_closed': '📪',
    'mailbox_with_mail': '📬',
    'mailbox_with_no_mail': '📭',
    'man': '👨',
    'man_with_gua_pi_mao': '👲',
    'man_with_turban': '👳',
    'mans_shoe': '👞',
    'maple_leaf': '🍁',
    'mask': '😷',
    'massage': '💆',
    'meat_on_bone': '🍖',
    'mega': '📣',
    'melon': '🍈',
    'memo': '📝',
    'mens': '🚹',
    'metal': '🤘',
    'metro': '🚇',
    'microphone': '🎤',
    'microscope': '🔬',
    'milky_way': '🌌',
    'minibus': '🚐',
    'minidisc': '💽',
    'mobile_phone_off': '📴',
    'money_with_wings': '💸',
    'moneybag': '💰',
    'monkey': '🐒',
    'monkey_face': '🐵',
    'monorail': '🚝',
    'mortar_board': '🎓',
    'mount_fuji': '🗻',
    'mountain_bicyclist': '🚵',
    'mountain_cableway': '🚠',
    'mountain_railway': '🚞',
    'mouse': '🐭',
    'mouse2': '🐁',
    'movie_camera': '🎥',
    'moyai': '🗿',
    'muscle': '💪',
    'mushroom': '🍄',
    'musical_keyboard': '🎹',
    'musical_note': '🎵',
    'musical_score': '🎼',
    'mute': '🔇',
    'nail_care': '💅',
    'name_badge': '📛',
    'necktie': '👔',
    'negative_squared_cross_mark': '❎',
    'neutral_face': '😐',
    'new': '🆕',
    'new_moon': '🌑',
    'new_moon_with_face': '🌚',
    'newspaper': '📰',
    'ng': '🆖',
    'nine': '9️⃣',
    'no_bell': '🔕',
    'no_bicycles': '🚳',
    'no_entry': '⛔️',
    'no_entry_sign': '🚫',
    'no_good': '🙅',
    'no_mobile_phones': '📵',
    'no_mouth': '😶',
    'no_pedestrians': '🚷',
    'no_smoking': '🚭',
    'non-potable_water': '🚱',
    'nose': '👃',
    'notebook': '📓',
    'notebook_with_decorative_cover': '📔',
    'notes': '🎶',
    'nut_and_bolt': '🔩',
    'o': '⭕️',
    'o2': '🅾️',
    'ocean': '🌊',
    'octopus': '🐙',
    'oden': '🍢',
    'office': '🏢',
    'ok': '🆗',
    'ok_hand': '👌',
    'ok_woman': '🙆',
    'older_man': '👴',
    'older_woman': '👵',
    'on': '🔛',
    'oncoming_automobile': '🚘',
    'oncoming_bus': '🚍',
    'oncoming_police_car': '🚔',
    'oncoming_taxi': '🚖',
    'one': '1️⃣',
    'open_file_folder': '📂',
    'open_hands': '👐',
    'open_mouth': '😮',
    'ophiuchus': '⛎',
    'orange_book': '📙',
    'outbox_tray': '📤',
    'ox': '🐂',
    'package': '📦',
    'page_facing_up': '📄',
    'page_with_curl': '📃',
    'pager': '📟',
    'palm_tree': '🌴',
    'panda_face': '🐼',
    'paperclip': '📎',
    'parking': '🅿️',
    'part_alternation_mark': '〽',
    'partly_sunny': '⛅️',
    'passport_control': '🛂',
    'paw_prints': '🐾',
    'peach': '🍑',
    'pear': '🍐',
    'pencil': '📝',
    'pencil2': '✏️',
    'penguin': '🐧',
    'pensive': '😔',
    'performing_arts': '🎭',
    'persevere': '😣',
    'person_frowning': '🙍',
    'person_with_blond_hair': '👱',
    'person_with_pouting_face': '🙎',
    'phone': '☎️',
    'pig': '🐷',
    'pig2': '🐖',
    'pig_nose': '🐽',
    'pill': '💊',
    'pineapple': '🍍',
    'pisces': '♓️',
    'pizza': '🍕',
    'plus1': '👍',  # an alias to +1
    'point_down': '👇',
    'point_left': '👈',
    'point_right': '👉',
    'point_up': '☝️',
    'point_up_2': '👆',
    'police_car': '🚓',
    'poodle': '🐩',
    'poop': '💩',
    'post_office': '🏣',
    'postal_horn': '📯',
    'postbox': '📮',
    'potable_water': '🚰',
    'pouch': '👝',
    'poultry_leg': '🍗',
    'pound': '💷',
    'pouting_cat': '😾',
    'pray': '🙏',
    'princess': '👸',
    'punch': '👊',
    'purple_heart': '💜',
    'purse': '👛',
    'pushpin': '📌',
    'put_litter_in_its_place': '🚮',
    'question': '❓',
    'rabbit': '🐰',
    'rabbit2': '🐇',
    'racehorse': '🐎',
    'radio': '📻',
    'radio_button': '🔘',
    'rage': '😡',
    'railway_car': '🚃',
    'rainbow': '🌈',
    'raised_hand': '✋',
    'raised_hands': '🙌',
    'raising_hand': '🙋',
    'ram': '🐏',
    'ramen': '🍜',
    'rat': '🐀',
    'recycle': '♻️',
    'red_car': '🚗',
    'red_circle': '🔴',
    'registered': '®️',
    'relaxed': '☺️',
    'relieved': '😌',
    'repeat': '🔁',
    'repeat_one': '🔂',
    'restroom': '🚻',
    'revolving_hearts': '💞',
    'rewind': '⏪',
    'ribbon': '🎀',
    'rice': '🍚',
    'rice_ball': '🍙',
    'rice_cracker': '🍘',
    'rice_scene': '🎑',
    'ring': '💍',
    'rocket': '🚀',
    'roller_coaster': '🎢',
    'rooster': '🐓',
    'rose': '🌹',
    'rotating_light': '🚨',
    'round_pushpin': '📍',
    'rowboat': '🚣',
    'ru': '🇷🇺',
    'rugby_football': '🏉',
    'runner': '🏃',
    'running': '🏃',
    'running_shirt_with_sash': '🎽',
    'sa': '🈂',
    'sagittarius': '♐️',
    'sailboat': '⛵️',
    'sake': '🍶',
    'sandal': '👡',
    'santa': '🎅',
    'satellite': '📡',
    'satisfied': '😆',
    'saxophone': '🎷',
    'school': '🏫',
    'school_satchel': '🎒',
    'scissors': '✂️',
    'scorpius': '♏️',
    'scream': '😱',
    'scream_cat': '🙀',
    'scroll': '📜',
    'seat': '💺',
    'secret': '㊙',
    'see_no_evil': '🙈',
    'seedling': '🌱',
    'seven': '7️⃣',
    'shaved_ice': '🍧',
    'sheep': '🐑',
    'shell': '🐚',
    'ship': '🚢',
    'shirt': '👕',
    'shit': '💩',
    'shoe': '👞',
    'shower': '🚿',
    'signal_strength': '📶',
    'simple_smile': '🙂',  # slightly smiling face
    'six': '6️⃣',
    'six_pointed_star': '🔯',
    'ski': '🎿',
    'skull': '💀',
    'sleeping': '😴',
    'sleepy': '😪',
    'slot_machine': '🎰',
    'small_blue_diamond': '🔹',
    'small_orange_diamond': '🔸',
    'small_red_triangle': '🔺',
    'small_red_triangle_down': '🔻',
    'smile': '😄',
    'smile_cat': '😸',
    'smiley': '😃',
    'smiley_cat': '😺',
    'smiling_imp': '😈',
    'smirk': '😏',
    'smirk_cat': '😼',
    'smoking': '🚬',
    'snail': '🐌',
    'snake': '🐍',
    'snowboarder': '🏂',
    'snowflake': '❄️',
    'snowman': '⛄️',
    'sob': '😭',
    'soccer': '⚽️',
    'soon': '🔜',
    'sos': '🆘',
    'sound': '🔉',
    'space_invader': '👾',
    'spades': '♠️',
    'spaghetti': '🍝',
    'sparkle': '❇️',
    'sparkler': '🎇',
    'sparkles': '✨',
    'sparkling_heart': '💖',
    'speak_no_evil': '🙊',
    'speaker': '🔈',
    'speech_balloon': '💬',
    'speedboat': '🚤',
    'star': '⭐️',
    'star2': '🌟',
    'stars': '🌠',
    'station': '🚉',
    'statue_of_liberty': '🗽',
    'steam_locomotive': '🚂',
    'stew': '🍲',
    'straight_ruler': '📏',
    'strawberry': '🍓',
    'stuck_out_tongue': '😛',
    'stuck_out_tongue_closed_eyes': '😝',
    'stuck_out_tongue_winking_eye': '😜',
    'sun_with_face': '🌞',
    'sunflower': '🌻',
    'sunglasses': '😎',
    'sunny': '☀️',
    'sunrise': '🌅',
    'sunrise_over_mountains': '🌄',
    'surfer': '🏄',
    'sushi': '🍣',
    'suspension_railway': '🚟',
    'sweat': '😓',
    'sweat_drops': '💦',
    'sweat_smile': '😅',
    'sweet_potato': '🍠',
    'swimmer': '🏊',
    'symbols': '🔣',
    'syringe': '💉',
    'tada': '🎉',
    'tanabata_tree': '🎋',
    'tangerine': '🍊',
    'taurus': '♉️',
    'taxi': '🚕',
    'tea': '🍵',
    'telephone': '☎️',
    'telephone_receiver': '📞',
    'telescope': '🔭',
    'tennis': '🎾',
    'tent': '⛺️',
    'thought_balloon': '💭',
    'three': '3️⃣',
    'thumbsdown': '👎',
    'thumbsup': '👍',
    'ticket': '🎫',
    'tiger': '🐯',
    'tiger2': '🐅',
    'tired_face': '😫',
    'tm': '™️',
    'toilet': '🚽',
    'tokyo_tower': '🗼',
    'tomato': '🍅',
    'tongue': '👅',
    'top': '🔝',
    'tophat': '🎩',
    'tractor': '🚜',
    'traffic_light': '🚥',
    'train': '🚋',
    'train2': '🚆',
    'tram': '🚊',
    'triangular_flag_on_post': '🚩',
    'triangular_ruler': '📐',
    'trident': '🔱',
    'triumph': '😤',
    'trolleybus': '🚎',
    'trophy': '🏆',
    'tropical_drink': '🍹',
    'tropical_fish': '🐠',
    'truck': '🚚',
    'trumpet': '🎺',
    'tshirt': '👕',
    'tulip': '🌷',
    'turtle': '🐢',
    'tv': '📺',
    'twisted_rightwards_arrows': '🔀',
    'two': '2️⃣',
    'two_hearts': '💕',
    'two_men_holding_hands': '👬',
    'two_women_holding_hands': '👭',
    'u5272': '🈹',
    'u5408': '🈴',
    'u55b6': '🈺',
    'u6307': '🈯',
    'u6708': '🈷',
    'u6709': '🈶',
    'u6e80': '🈵',
    'u7121': '🈚',
    'u7533': '🈸',
    'u7981': '🈲',
    'u7a7a': '🈳',
    'uk': '🇬🇧',
    'umbrella': '☔️',
    'unamused': '😒',
    'underage': '🔞',
    'unlock': '🔓',
    'up': '🆙',
    'us': '🇺🇸',
    'v': '✌️',
    'vertical_traffic_light': '🚦',
    'vhs': '📼',
    'vibration_mode': '📳',
    'video_camera': '📹',
    'video_game': '🎮',
    'violin': '🎻',
    'virgo': '♍️',
    'volcano': '🌋',
    'vs': '🆚',
    'walking': '🚶',
    'waning_crescent_moon': '🌘',
    'waning_gibbous_moon': '🌖',
    'warning': '⚠️',
    'watch': '⌚️',
    'water_buffalo': '🐃',
    'watermelon': '🍉',
    'wave': '👋',
    'wavy_dash': '〰️',
    'waxing_crescent_moon': '🌒',
    'waxing_gibbous_moon': '🌔',
    'wc': '🚾',
    'weary': '😩',
    'wedding': '💒',
    'whale': '🐳',
    'whale2': '🐋',
    'wheelchair': '♿️',
    'white_check_mark': '✅',
    'white_circle': '⚪️',
    'white_flower': '💮',
    'white_large_square': '⬜️',
    'white_medium_small_square': '◽️',
    'white_medium_square': '◻️',
    'white_small_square': '▫️',
    'white_square_button': '🔳',
    'wind_chime': '🎐',
    'wine_glass': '🍷',
    'wink': '😉',
    'wolf': '🐺',
    'woman': '👩',
    'womans_clothes': '👚',
    'womans_hat': '👒',
    'womens': '🚺',
    'worried': '😟',
    'wrench': '🔧',
    'x': '❌',
    'yellow_heart': '💛',
    'yen': '💴',
    'yum': '😋',
    'zap': '⚡️',
    'zero': '0️⃣',
    'zzz': '💤',
}


def _replace_emoji(line):
    for shortcode, characters in _emoji_replacement_mapping.items():
        line = line.replace(':{}:'.format(shortcode), characters)
    return line


def _unreplace_emoji(line):
    # replace sequences before single characters
    for shortcode, character in sorted(
            _emoji_replacement_mapping.items(),
            key=lambda t: len(t[1]),
            reverse=True
    ):
        line = line.replace(character, ':{}:'.format(shortcode))
    return line


def do_the_thing(func):
    conn = op.get_bind()

    for table_name, column_name in (('posts', 'content'),
                                    ('messages', 'message')):
        table = sa.Table(
            table_name,
            sa.MetaData(),
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column(column_name, sa.String)
        )
        for row in conn.execute(table.select()):
            content = getattr(row, column_name)
            new_content = func(content)
            if not new_content == content:
                conn.execute(
                    table.update().where(
                        table.c.id == row.id
                    ).values(**{column_name: new_content})
                )


def upgrade():
    do_the_thing(_replace_emoji)


def downgrade():
    do_the_thing(_unreplace_emoji)
