# 排序与查找算法演示

一个可以直接运行的 Python 算法练习，包含冒泡排序、顺序查找和二分查找。

## 运行

需要 Python 3.9 或更新版本，无需安装第三方库。

```text
python main.py 8 3 5 1 --target 5
```

程序会输出排序后的列表，以及目标数字在排序结果中的位置。位置从 0 开始。如果没有提供 `--target`，只进行排序。

## 三种算法

| 函数 | 用途 | 时间复杂度 |
| --- | --- | --- |
| `bubble_sort(numbers)` | 返回升序排列的新列表 | O(n²) |
| `linear_search(numbers, target)` | 从头查找，返回首次出现的位置 | O(n) |
| `binary_search(sorted_numbers, target)` | 在已排序列表中查找 | O(log n) |

找不到目标时，查找函数返回 `-1`。`bubble_sort` 不修改传入的原列表。调用二分查找前，必须先按升序排序。

## 测试

```text
python -m unittest discover -s tests -v
```

本程序只处理命令行中给出的整数，不联网，也不保存数据。许可证见 [LICENSE](LICENSE)。
