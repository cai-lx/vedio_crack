# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 23:10:44 2025

Refactored version: renamed to `vedio_crack.py`, UI converted to grid layout,
URL-building extracted to `build_parser_url` with minimal validation.
"""

import tkinter
import tkinter.messagebox as messagebox
import webbrowser
import re


def build_parser_url(video_url: str) -> str:
    """构建第三方解析器 URL，并做最小的校验。

    要求非空且以 http:// 或 https:// 开头。失败时抛出 ValueError。
    返回拼接后的完整解析器 URL。
    """
    if not video_url or not video_url.strip():
        raise ValueError("empty url")
    url = video_url.strip()
    if not re.match(r'^https?://', url, flags=re.I):
        raise ValueError("invalid url")
    return 'https://jx.xmflv.com/?url=' + url


class VIPVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('VIP追剧神器')
        self.root.geometry('520x140')
        # 设置窗口关闭协议
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # 不允许用户改变大小，保持布局稳定
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # 恢复为原始的 place() 绝对布局，使控件更紧凑（与原始 UI 对齐）
        label_movie_link = tkinter.Label(self.root, text='输入视频网址：')
        label_movie_link.place(x=20, y=30, width=100, height=30)

        self.entry_movie_link = tkinter.Entry(self.root)
        self.entry_movie_link.place(x=125, y=30, width=260, height=30)

        button_clear = tkinter.Button(self.root, text='清空', command=self.empty)
        button_clear.place(x=400, y=30, width=50, height=30)

        btn_iqy = tkinter.Button(self.root, text='爱奇艺', command=self.open_iqy)
        btn_iqy.place(x=25, y=80, width=80, height=40)

        btn_tx = tkinter.Button(self.root, text='腾讯', command=self.open_tx)
        btn_tx.place(x=125, y=80, width=80, height=40)

        btn_yk = tkinter.Button(self.root, text='优酷', command=self.open_yq)
        btn_yk.place(x=225, y=80, width=80, height=40)

        btn_play = tkinter.Button(self.root, text='播放', command=self.play_video)
        btn_play.place(x=325, y=80, width=125, height=40)

        # 初始时让输入框获取焦点
        self.entry_movie_link.focus_set()

    def open_iqy(self):
        webbrowser.open('https://www.iqiyi.com')

    def open_tx(self):
        webbrowser.open('https://v.qq.com')

    def open_yq(self):
        webbrowser.open('https://www.youku.com/')

    def play_video(self):
        video = self.entry_movie_link.get()
        try:
            parser_url = build_parser_url(video)
        except ValueError:
            messagebox.showerror('输入错误', '请输入有效的视频 URL，需以 http:// 或 https:// 开头')
            return
        webbrowser.open(parser_url)

    def empty(self):
        self.entry_movie_link.delete(0, 'end')
        self.entry_movie_link.focus_set()

    def on_closing(self):
        try:
            self.root.destroy()
        finally:
            try:
                self.root.quit()
            except Exception:
                pass


if __name__ == '__main__':
    root = tkinter.Tk()
    app = VIPVideoApp(root)
    root.mainloop()
