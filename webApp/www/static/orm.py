#coding: utf -8

'我们先考虑如何定义一个User对象，然后把数据库表users和它关联起来。'

__author__ = 'sunyunpeng'


class Field(object):
	"""docstring for Field"""
	def __init__(self, name, column_type, primary_key, default):
		self.name = name
		self.column_type = column_type
		self.primary_key = primary_key
		self.default = default

	def __str__(self):
		return '<%s, %s:%s >' % (self.__class__.__name__, self.column_type, self.name)


class StringFeild(Field):
	"""docstring for StringFeild"""
	def __init__(self, name = None, primary_key = False, default = None, column_type = 'varchar(100)'):
		super().__init__(name, column_type, primary_key, default)		


class IntegerField(Field):
	"""docstring for IntegerField"""
	def __init__(self, name = None, default = None, column_type = 'bigint'):
		super().__init__(name, column_type, primary_key, default)	

class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		tableName = attrs.get('__table__', None) or name
		logging.info('found model: %s (table: %s)' % (name, tableName))
		mappings = dict()
		fields = []
		primaryKey = None
		for k, v in attrs.items():
			if isinstance(v, Field):
				logging.info('  found mapping: %s ==> %s' % (k, v))
				mapings[k] =v
				if v.primary_key:
					if primaryKey:
						raise RuntimeError('Duplicate primary key for field: %s' % k)
					primaryKey = k
				else:
					fields.append(k)
		if not primaryKey:
			raise RuntimeError('Primary key not found.')
		for k in mappings.items():
			attrs.pop()

		escaped_feilds = list(map(lambda f: '`%s`' %f, fields))
		attrs['__mapping__'] = mapings
		attrs['__table__'] = tableName
		attrs['__fields__'] = fields
		# 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)
		


class Model(dict, metaclass = ModelMetaclass):
	"""docstring for Model"""
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def getValue(self, key):
		return getattr(self, key, None)

	def getValueOrDefault(self, key):
		value = getattr(self, key, None)
		if value is None:
			field = self.__mapping__[key]
			if field.default is not None:
				value = field.default() if callable(field.default) else field.default
				logging.debug('using default value for %s: %s' % (key, str(value)))
				setattr(self, key, value)
		return value

class User(Model):
	__table__ = 'users'
	id = IntegerField(primary_key = True)
	name = StringFeild()
		






		
