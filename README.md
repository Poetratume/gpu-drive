# GPU Dive

一个不带站点导航或教学面板的 GPU 逐层探索组件。全英文 UI，无需依赖、构建工具、服务器或联网。

## 直接打开

双击 `index.html`。产品图片已内嵌，离线可用。

- 点击显卡 → 电路板 → GPU → SM → 执行分区 → CUDA Core。
- SM 底部橙色分支：示例驻留 Block → Warp → Thread。
- 缓存、显存、寄存器、Tensor Core、RT Core 可以分别查看。
- 左上角返回、层级路径或 Esc 返回上层；右上角可回到显卡或全屏。
- 内部只表示架构关系，不是实际 PCB / die floorplan；绿色是物理硬件，橙色是示例逻辑任务。
- 最深层是功能单元或线程状态，不是晶体管电路。未包含任务运行模拟。

## 嵌入自己的网页

将 `gpu-dive.js` 放到网站目录，然后加入：

```html
<gpu-dive style="display:block; width:100%; height:760px; border-radius:20px; overflow:hidden;"></gpu-dive>
<script src="/your-path/gpu-dive.js"></script>
```

组件使用 Shadow DOM，内部样式与外部页面隔离。它会根据组件容器宽度切换为纵向布局。建议至少 440px 高；桌面 700–850px 高。

`embed.html` 是一个可直接打开的嵌入示例。如果你的网页框架只支持 iframe，也可以直接嵌入 `index.html`：

```html
<iframe src="/gpu-dive/index.html" title="GPU Dive"
  style="width:100%; height:760px; border:0; border-radius:20px;"
  allow="fullscreen"></iframe>
```

## 与网站交互（可选）

```js
document.querySelector('gpu-dive').addEventListener('gpu-dive:change', event => {
  console.log(event.detail.level, event.detail.path);
});
```

## 修改源码

- `src/gpu-dive.template.js`：可读的组件源码；`__CARD_DATA__` 由打包脚本填入。
- `assets/card.png`：ASUS 官方产品图。
- `build.py`：使用 Python 3 标准库生成 `gpu-dive.js` 和独立 `index.html`。
- 修改后在这个目录运行 `python3 build.py`。

所有任务编号、存储单元排列、PCB 布局和逻辑驻留示例均为示意。4070 的 5,888 CUDA cores 与 Ada 每 SM 128 个 CUDA cores 对应 46 个启用的 SM。L1 和 Shared Memory 在 Ada 中共享物理存储资源，UI 按访问语义分开展示。

## 资料与图像来源

- 产品图与规格：[ASUS Dual GeForce RTX 4070](https://www.asus.com/motherboards-components/graphics-cards/dual/dual-rtx4070-12g/)
- 产品图原地址：https://dlcdnwebimgs.asus.com/gain/4670e704-97f5-4d00-9d17-e59593ba3dd3/
- [NVIDIA Ada architecture whitepaper](https://images.nvidia.com/aem-dam/Solutions/geforce/ada/nvidia-ada-gpu-architecture.pdf)
- [NVIDIA Ada Tuning Guide](https://docs.nvidia.com/cuda/ada-tuning-guide/)
- [CUDA Programming Model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)

这些来源也可通过界面右上角的信息按钮打开。产品图保留原有品牌标识。
