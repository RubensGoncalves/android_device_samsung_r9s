#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/samsung/universal2100-common',
    'hardware/samsung_slsi-linaro/exynos',
    'hardware/samsung_slsi-linaro/graphics',
    'vendor/samsung/universal2100-common',
]

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib/sensors.sensorhub.so',
        'vendor/lib64/sensors.sensorhub.so'
    ): blob_fixup()
        .remove_needed('libhidltransport.so')
        .add_needed('libutils-v32.so')
        .binary_regex_replace(b'_ZN7android6Thread3runEPKcim', b'_ZN7utils326Thread3runEPKcim'),

    'vendor/lib64/libexynoscamera3.so': blob_fixup()
        .sig_replace('14 00 00 94 0A 00 00 14', '1F 20 03 D5 0A 00 00 14')
        .sig_replace('A8 FF FF 97 0A 00 00 14', '1F 20 03 D5 0A 00 00 14')
        .sig_replace('AB 02 20 36', '1F 20 03 D5')
        .add_needed('libshim_ui.so'),

    'vendor/lib/libexynoscamera3.so': blob_fixup()
        .sig_replace('14 00 00 94 0A 00 00 14', '1F 20 03 D5 0A 00 00 14')
        .sig_replace('A8 FF FF 97 0A 00 00 14', '1F 20 03 D5 0A 00 00 14')
        .sig_replace('AB 02 20 36', '1F 20 03 D5')
        .add_needed('libshim_ui.so'),

    (
        'vendor/lib/soundfx/libaudioeffectoffload.so',
        'vendor/lib64/soundfx/libaudioeffectoffload.so'
    ): blob_fixup()
        .replace_needed('libtinyalsa.so', 'libtinyalsa.exynos2100.so'),

    'vendor/lib/hw/audio.primary.exynos2100.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute.exynos2100.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa.exynos2100.so'),

    (
        'vendor/lib/libaudioproxy2.so',
        'vendor/lib/libaudioparamupdate.so',
        'vendor/lib64/libaudioparamupdate.so',
        'vendor/lib/libaboxpcmdump.so'
    ): blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute.exynos2100.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa.exynos2100.so'),

    'vendor/lib64/libaudioroute.exynos2100.so': blob_fixup()
        .replace_needed('libtinyalsa.so', 'libtinyalsa.exynos2100.so'),
    'vendor/lib/libaudioroute.exynos2100.so': blob_fixup()
        .replace_needed('libtinyalsa.so', 'libtinyalsa.exynos2100.so'),

    'vendor/lib/libsynaFpSensorTestNwd.so': blob_fixup()
    .add_needed('lib_lvacfs.so')
} # fmt: skip

module = ExtractUtilsModule(
    'o1s',
    'samsung',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'universal2100-common', module.vendor
    )
    utils.run()

