import string


class _formatter(string.Formatter):
    def format_field(self, value, format_spec):
        if isinstance(value, str):
            if format_spec.endswith('u'):
                value = value.upper()
                format_spec = format_spec[:-1]
            elif format_spec.endswith('l'):
                value = value.lower()
                format_spec = format_spec[:-1]
        return super(_formatter, self).format(value, format_spec)


fmt = _formatter()
