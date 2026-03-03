# 操作手册 - S01-17 再次面对沈清起

> **按以下步骤操作即可，无需思考**

---

## 第一步：生成首帧图

1. 打开 **Nano Banana Pro**
2. 上传参考图（按顺序）：
   - 辛月影-三视图.png
   - 沈清起-三视图.png
   - 破旧草屋-定场镜头.png
3. 打开 `first_frame.md`，复制其中的完整提示词
4. 点击生成
5. 保存为：`shot_017_first_frame.png`

---

## 第二步：生成尾帧图

1. 打开 **Nano Banana Pro**
2. 上传参考图（按顺序）：
   - shot_017_first_frame.png（刚才生成的首帧）
   - 沈清起-表情卡.png
3. 打开 `last_frame.md`，复制其中的完整提示词
4. 点击生成
5. 保存为：`shot_017_last_frame.png`

---

## 第三步：生成9分镜组合图

1. 打开 **Nano Banana Pro**
2. 上传参考图（按顺序）：
   - shot_017_first_frame.png
   - 辛月影-三视图.png
   - 沈清起-三视图.png
3. 打开 `storyboard_grid.md`，复制其中的完整提示词
4. 点击生成
5. 保存为：`shot_017_storyboard_grid.png`

---

## 第四步：生成视频（可灵）

1. 打开 **可灵动画**
2. 选择模型：**视频 2.6**
3. 选择时长：**5秒**
4. 上传图片（按顺序，最多5张）：
   - shot_017_first_frame.png（首帧钉定）
   - shot_017_last_frame.png（尾帧钉定）
   - shot_017_storyboard_grid.png（动作参考）
   - 辛月影-三视图.png（角色一致性）
   - 破旧草屋-定场镜头.png（场景一致性）
5. 打开 `video_prompt.md`，复制其中的完整提示词
6. 点击生成
7. 保存为：`shot_017_video.mp4`

---

## 检查清单

- [ ] 首帧图已生成并保存
- [ ] 尾帧图已生成并保存
- [ ] 9分镜组合图已生成并保存
- [ ] 视频已生成并保存
