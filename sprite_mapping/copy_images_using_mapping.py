import csv
import os
import shutil

output_base_path = r'c:\temp\ps3_output'
old_sprite_base_path = r'C:\games\Steam\steamapps\common\Umineko Chiru\NSA_ext\big'

with open('mapping_custom.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for i, row in enumerate(reader):
        if i == 0:
            continue

        ps3_filepath = row[0] #already has .png
        old_filepath = row[1] + '.png'

        invalid = False
        if 'sprites' in old_filepath:
            print(f"invalid old filepath {old_filepath}")
            invalid = True

        if 'bmp' in ps3_filepath:
            print(f"invalid ps3 filepath {ps3_filepath}")
            invalid = True

        if invalid:
            continue

        full_ps3_filepath = os.path.join(output_base_path, ps3_filepath)
        full_old_sprite_filepath = os.path.join(old_sprite_base_path, old_filepath)

        if not os.path.exists(full_old_sprite_filepath):
            print(f"Old sprite missing! {full_old_sprite_filepath} (from {full_ps3_filepath})")
            continue

        # print(f'copying {ps3_filepath} -> {old_filepath}')
        os.makedirs(os.path.dirname(full_ps3_filepath), exist_ok=True)
        shutil.copy(full_old_sprite_filepath, full_ps3_filepath)



# zoom folder is handled separately! images should have the same file names, so should be easy.