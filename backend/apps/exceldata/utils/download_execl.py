# -*- coding: utf-8 -*-
from django.http import HttpResponse
import urllib.parse


class DownloadExcel:
    def __init__(self):
        pass

    @staticmethod
    def gen_response(output_io, filename):
        """
        生成文件下载响应
        :param output_io: 文件内容
        :param filename: 文件名
        :return: HttpResponse
        """
        response = HttpResponse(
            output_io,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        # 使用 utf-8 编码文件名
        file_name = filename
        encoded_file_name = urllib.parse.quote(file_name)
        response[
            'Content-Disposition'] = f'attachment; filename="{encoded_file_name}"; filename*=UTF-8\'\'{encoded_file_name}'

        return response
