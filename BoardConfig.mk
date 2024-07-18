#
# Copyright (C) 2022 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## Inherit from the common tree
include device/samsung/universal2100-common/BoardConfigCommon.mk

# Inherit from the proprietary configuration
include vendor/samsung/r9s/BoardConfigVendor.mk

DEVICE_PATH := device/samsung/r9s

# APEX image
DEXPREOPT_GENERATE_APEX_IMAGE := true

# Camera
# ID=52 is telephoto camera
# ID=56
# ID=58
SOONG_CONFIG_samsungCameraVars_extra_ids := 52,56,58

# Display
TARGET_SCREEN_DENSITY := 410

# Kernel
TARGET_KERNEL_CONFIG := exynos2100-r9sxxx_defconfig

# Kernel modules
BOARD_VENDOR_RAMDISK_KERNEL_MODULES_LOAD := $(strip $(shell cat $(DEVICE_PATH)/modules.load))
BOOT_KERNEL_MODULES := $(BOARD_VENDOR_RAMDISK_KERNEL_MODULES_LOAD)
BOARD_RECOVERY_RAMDISK_KERNEL_MODULES_LOAD := $(strip $(shell cat $(DEVICE_PATH)/modules.load))
RECOVERY_KERNEL_MODULES := $(BOARD_RECOVERY_RAMDISK_KERNEL_MODULES_LOAD)

TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop
