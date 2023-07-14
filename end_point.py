# projects informations endd point

projects_endpoint="https://youtrack22.onedatasoftware.com/api/admin/projects?$top=-1&fields=name,ringId"
project_endpint='https://youtrack22.onedatasoftware.com/hub/api/rest/projects/{Project_ring_id}/team?fields=name,users(name,profile(email)),project/owner'

# users informations endpint
users_endpoint="https://youtrack22.onedatasoftware.com/api/users?$top=-1&fields=name,ringId&banned=false"
user_endpoint="https://youtrack22.onedatasoftware.com/hub/api/rest/users/{user_ring_id}?$top=-1&fields=eraseTimestamp,banReason,banned,banBadge,login,name,profile(email,jabber,avatar)"