
# Serializers are used to allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON , XML or #other content types.
# basic crud operations is achieved as visible in screenshots
#
#
#
#
#  query for a max of 20 tickets to be booked at a time 
# If len(objects.all()) <= 20 : return True
# if abs(obj.time() - datetime.time.now()) >= 8 then pass
#            Else res.append(obj)
#
#
#
# for diff of 8 hours:
#   datetime.now()-queryset.created
#
#
#
# When a customer books ticket , time is automatically assigned at the time of ticket processing
# using   ->>      created = models.DateTimeField(auto_now=True)
