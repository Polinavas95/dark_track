from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext as _
from django.core.validators import FileExtensionValidator

class MaxSizeValidator(MaxValueValidator):
    message = _('The file exceed the maximum size of %(limit_value)s MB.')

    def __call__(self, value):
        cleaned = self.clean(value.size)
        params = {'limit_value': self.limit_value, 'show_value': cleaned, 'value': value}
        if self.compare(cleaned, self.limit_value * 1024 * 1024):
            raise ValidationError(self.message, code=self.code, params=params)


SHAPE_VALIDATORS = dict([(ext, FileExtensionValidator(allowed_extensions=[ext])) for ext in ("shp", "shx", "dbf")])