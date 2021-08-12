from django.test import TestCase

# Create your tests here.
# {  # <table align="center" border="1">#}
#     {  # <tr><th colspan="7">All Student Details</th></tr>#}
#         {  # <tr>#}
#             {  # <th>Name</th>#}
#                 {  # <th>{{ object.name }}</th>#}
#                     {  # </tr>#}
#                         {  # <tr>#}
#                             {  # <th>Age</th>#}
#                                 {  # <th>{{ object.age }}</th>#}
#                                     {  # </tr>#}
#                                         {  # <tr>#}
#                                             {  # <th>Contact</th>#}
#                                                 {  # <th>{{ object.contact }}</th>#}
#                                                     {  # </tr>#}
#                                                         {  # <tr>#}
#                                                             {  # <th>Email</th>#}
#                                                                 {  # <th>{{ object.email }}</th>#}
#                                                                     {  # </tr>#}
#                                                                         {  # <tr>#}
#                                                                             {  # <th>Image</th>#}
#                                                                                 {
#                                                                                     <th><img src="{{ object.image.url }}" width="100" height="100" alt=""></th>#}
                                                                                    # {  # </tr>#}
                                                                                    #     {  # <tr>#}
                                                                                    #         {
                                                                                    #             <th colspan="2"><a href="{% url 'update'  %}?name={{ object.name }}">Update</a></th>#}
                                                                                                # {  # </tr>#}
                                                                                                #     {  # <tr>#}
                                                                                                #         {
                                                                                                #             <th colspan="2"><a href="{% url 'delete'  %}?name={{ object.name }}">Delete</a></th>#}
                                                                                                            # {  # </tr>#}
                                                                                                            #     {  ##}
                                                                                                            #         {
                                                                                                                        #}
                                                                                                                        # {  # </table>#}
