---
id: cz2n6itkjgdlaj21rbrx5h6
title: Computer Graphics
desc: ""
updated: 1709506829846
created: 1709066522582
---

## [NeRF](https://www.matthewtancik.com/nerf)

- https://towardsdatascience.com/nerf-and-what-happens-when-graphics-becomes-differentiable-88a617561b5d
- https://pyimagesearch.com/2021/11/10/computer-graphics-and-deep-learning-with-nerf-using-tensorflow-and-keras-part-1/

## [TensorFlow Graphics](https://github.com/tensorflow/graphics/)

Let's delve into each of these questions:

1. **Geometric interpretation of the determinant in 3D**:
   The determinant in 3D can be interpreted geometrically as the signed volume of a parallelepiped defined by the vectors formed by the rows or columns of a 3x3 matrix. If the determinant is zero, it means the three vectors are linearly dependent, and the volume collapses to zero, indicating that the parallelepiped is degenerate or flat.

2. **Aliasing**:
   Aliasing refers to the jagged or stair-stepped appearance of curved or diagonal lines in digital images or computer graphics, especially when those lines should be smooth. It occurs due to the discrete nature of digital representations, where high-frequency components (detail) in an image exceed the sampling rate or resolution of the display or rendering process.

3. **Representation of 3D models and triangles**:
   Triangles are used extensively in 3D models because they are simple primitives that are easy to work with mathematically. They form the basis for rendering graphics efficiently, as they are planar and can be rasterized quickly. Other representations include polygons (quads, pentagons, etc.), spline-based surfaces (Bezier surfaces, NURBS), and voxel-based representations. Each has its advantages and contexts in which they are useful, but triangles remain dominant due to their simplicity and efficiency in rendering algorithms.

4. **Z-buffer in real-time 3D engines**:
   A Z-buffer (or depth buffer) stores the depth (Z-coordinate) of each pixel in a rendered scene. This information is used to determine which objects or parts of objects are visible in a particular view. The main advantage of a Z-buffer is its simplicity and efficiency in handling occlusion in real-time rendering. However, a potential drawback is the memory consumption, especially at higher resolutions or with complex scenes.

5. **Selection of mip level by GPU**:
   The GPU typically selects the mip level based on the size of the texture on the screen relative to its original size and the distance of the object from the viewer. The goal is to minimize aliasing and texture shimmering while maximizing performance. This selection is often done automatically by the GPU hardware based on predefined algorithms.

6. **Vertex shader output to pixel shader**:
   Data output by the vertex shader typically includes attributes such as position, normal, texture coordinates, and any other interpolated values. This data is interpolated across the pixels of each triangle and fed into the pixel shader, where per-pixel computations, such as lighting and texturing, are performed.

7. **Representation of 3D rotations**:
   3D rotations can be represented using various methods such as Euler angles, axis-angle representation, quaternion, or rotation matrices. Each has its pros and cons in terms of mathematical simplicity, compactness, numerical stability, and ease of interpolation.

8. **Ray-triangle intersection in ray tracing**:
   When implementing a ray-triangle intersection function, attention should be paid to handling cases where the ray and triangle are coplanar or parallel, ensuring numerical stability to avoid division by zero or floating-point inaccuracies, and optimizing for performance since this operation is often a bottleneck in ray tracing algorithms.

9. **Representation of colors**:
   Colors can be represented on a computer using various color models such as RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value), or CIE Lab. Each has its advantages and contexts in which they are useful, but RGB is the most commonly used model in computer graphics due to its direct correspondence with display hardware.

10. **Compression of video game data**:
    To compress the data of a video game, various techniques can be employed such as texture compression (e.g., using DXT formats), level of detail (LOD) techniques for reducing the complexity of geometry or textures at a distance, hierarchical data structures (e.g., octrees) for efficient storage and rendering of terrain data, and procedural generation techniques to generate content on-the-fly instead of storing it directly. Each of these approaches aims to balance compression ratio with visual quality and runtime performance.

- Culling: remove object not visible to the player from the frame
  - occlusion culling: optimize performance by render only what visible by the player + don’t render hidden object
  - frsutum culling: player field of view cone
- LODS : level of detail

Here are a few questions related to computer graphics.

Most questions are with no single answer. You can discuss as much as you like
to show what you know about the topic.

If you need, you can do a research on the internet to refresh your memory but
we ask that you understand the answer you write.

If you can't answer some questions, that's ok.

You can write your answers in English or French, as you prefer.

===============================================================================

- Give a geometric interpretation for the determinant in 3D

- What is aliasing?

- 3D models can be made of triangles. Why? Are there other representations? In
  which context can they be used?

- In the context of a real-time 3D engine, what would you put in a Z-buffer?
  What are the pros and cons?

- How does the GPU choose the mip of a texture to use?

- What happens to the data output by the vertex shader, how is it fed to the
  pixel shader stage ? Think of how you would implement it yourself
  in software.

- How can you represent 3D rotations on a computer? What are the pros and cons?

- In the context of raytracing, to what should you pay attention when
  implementing ray-triangle intersection function?

- How can you represent colors on a computer? What are the pros and cons?

- What would be your approach to compress the data of a video game as much as
  possible? For instance, the height maps used for representing a terrain.
