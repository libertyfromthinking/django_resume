from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

# 파일 이름에 thumb.jpg 또는 thumb.jpeg 붙임
def _add_thumb(s):
    parts = s.split('.')
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpeg'
    return '.'.join(parts)

# 시스템에 파일을 직접 쓰는 클래스
class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile,self).save(name,content,save)
        img = Image.open(self.path)

        size = (128,128)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGB', size, (255,255,255,0))
        background.paste(img, ( int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2) ))
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile,self).delete(save)

# 장고 모델 정의에 사용하는 필드
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
