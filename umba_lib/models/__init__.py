from settings.database import db
from settings.config import app


class BaseModelMixin:
    @staticmethod
    def create_(model_object, **kwargs):
        _model_object = model_object(**kwargs)
        db.session.add(_model_object)
        db.session.commit()

        return _model_object

    @staticmethod
    def list_(model_object, *, page=None, per_page=None, **kwargs):
        if page:
            per_page = per_page if per_page else app.config.get("PER_PAGE")
            return model_object.query.filter_by(**kwargs).paginate(page=page, per_page=per_page)
        return model_object.query.filter_by(**kwargs).all()

    @staticmethod
    def get_(model_object, **kwargs):
        instance = model_object.query.filter_by(**kwargs).first()

        if instance:
            return instance

        raise ValueError("object cannot be found from this model %s with this kwargs %s" % (model_object.__name__, str(kwargs)) )

    @staticmethod
    def delete_(model_object, **kwargs):
        model_object.query.filter_by(**kwargs).delete()
        db.session.commit()

    @staticmethod
    def delete_one_(model_object, pk):
        model_object.query.filter_by(id=pk).delete()
        db.session.commit()

    @staticmethod
    def update_one_(model_object, data, pk):
        model_object.query.filter_by(id=pk).update(data)
        db.session.commit()

    @staticmethod
    def update_(model_object, data, **kwargs):
        model_object.query.filter_by(**kwargs).update(**data)
        db.session.commit()


class ModelUtilities:
    @staticmethod
    def start():
        with app.app_context():
            db.create_all()

    @staticmethod
    def drop():
        with app.app_context():
            db.drop_all()

    @staticmethod
    def list(model_name, **kwargs):
        return BaseModelMixin.list_(model_name, **kwargs)

    @staticmethod
    def get(model_name, **kwargs):
        return BaseModelMixin.get_(model_name, **kwargs)

    @staticmethod
    def delete_one(model_name, pk):
        return BaseModelMixin.delete_one_(model_name, pk)

    @staticmethod
    def delete(model_name, **kwargs):
        return BaseModelMixin.delete_(model_name, **kwargs)

    @staticmethod
    def update_one(model_name, data, pk):
        return BaseModelMixin.update_one_(model_name, data, pk)

    @staticmethod
    def update(model_name, data, **kwargs):
        return BaseModelMixin.update_(model_name, data, **kwargs)

    @staticmethod
    def create(model_name, **kwargs):
        return BaseModelMixin.create_(model_name, **kwargs)
