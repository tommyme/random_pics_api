# Random pic api

### main.py

> 定义了sanic server 访问路由/random_pic的时候返回随机二次元图片

- 在服务器上投入使用

```python
# 这里的pic_list是从pickle里面读取的list，只是图片的文件名
selected = random.choice(pic_list)
# 这里就是把文件名进行一个格式化字符串的处理，可以改成cdn，也可以改成自己的服务器
pic_url = f"http://{selected}"
```
