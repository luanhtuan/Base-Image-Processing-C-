#pragma once

void CloneImage(byte* dest, byte* src, int size);

void GrayscaleImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void IncreaseBrightnessOfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void IncreaseContrastOfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void BoundingBoxImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void DecreaseOpacityOfHalfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void SplitingAndSortingImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void BlendingAreasOfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void ReplaceAnAreaOfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void FlipAnAreaOfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void ZoomOutAnAreaOfImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void ZoomInAndBlendingImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void InvertImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void CompressImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void DecompressImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void SimpleEncryptImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void BlurImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void MotionBlurImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void BloomImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void CCBlurImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void CCBloomImage(int width, int height, int byte_per_pixel, byte*& data, double value);
void EdgeImage(int width, int height, int byte_per_pixel, byte*& data, double value);

void GrayscaleImage(int width, int height, int byte_per_pixel, byte*& data, double value);

void MakeHalfImageTransparent(int width, int height, int byte_per_pixel, byte*& data, double value);
void FlipAnImageHorizontal(int width, int height, int byte_per_pixel, byte*& data, double value);
void FlipAnImageVertical(int width, int height, int byte_per_pixel, byte*& data, double value);
void CompressImageTo16bit(int width, int height, int byte_per_pixel, byte*& data, double value);
void SoftlightImage(int width, int height, int byte_per_pixel, byte *& data, double value);