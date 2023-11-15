from flask import request, make_response
from . import api, models
from .usecases.auth import token_required

# Importing all routes
from .usecases import auth
from ..utils import db


@api.route("/contacts/<int:contact_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/contacts/", methods=["GET", "POST"])
@token_required
def contacts_urls(contact_id=None):
    try:
        data = request.get_json()
    except:
        pass

    # Running contact operations

    if contact_id is not None:
        contact_object = models.Contact.query.get_or_404(
            ident=contact_id,
            description="The contact you're trying to fetch wasn't found. Please try again with a different contact_id",
        )

        match request.method:
            case "GET":
                return {
                    "id": contact_object.id,
                    "first_name": contact_object.first_name,
                    "last_name": contact_object.last_name,
                    "email": contact_object.email,
                    "local_phone": contact_object.local_phone,
                    "mobile_phone": contact_object.mobile_phone,
                    "user_id": contact_object.user_id,
                }, 200
            case "PUT":
                contact_object.first_name = data["first_name"]
                contact_object.last_name = data["last_name"]
                contact_object.local_phone = data["local_phone"]
                contact_object.mobile_phone = data["mobile_phone"]
                contact_object.email = data["email"]
                db.session.commit()
                return {"detail": f"Contact {contact_object.email} was modified!!"}, 200

            case "DELETE":
                """Deletes an existing pet"""

                db.session.delete(contact_object)
                db.session.commit()
                return {
                    "detail": f"Successfully deleted contact {contact_object.id}"
                }, 200

            case _:
                response = make_response()

                response.status_code = 400
                response.set_data("Bad request, please try again")
                return response

    # non contact specific operations

    contacts = models.Contact.query.all()

    match request.method:
        case "GET":
            return [
                {"id": contact.id, "name": contact.first_name} for contact in contacts
            ]

        case "POST":
            required_fields = [
                "first_name",
                "last_name",
                "local_phone",
                "mobile_phone",
                "email",
                "user_id",
            ]

            for field in required_fields:
                if field not in data:
                    return {"detail": f'"{field}" field is required'}, 400

            new_contact = models.Contact(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                mobile_phone=data["mobile_phone"],
                local_phone=data["local_phone"],
                user_id=data["user_id"],
            )

            db.session.add(new_contact)
            db.session.commit()

            return {
                "detail": f"Successfully created contact {new_contact.first_name}"
            }, 200

        case _:
            # Better than create a new request and then assign
            return {"detail": "Bad request, please try again"}, 400
