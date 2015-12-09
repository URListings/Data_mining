# Filter scripts

#Cal hacks
python filter_proj_fields.py proj/calhacks.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/calhacks/calhacks.json 1

#Tech crunch filter
python filter_proj_fields.py proj/techcrunch.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/techcrunch/techcrunch.json 1

#Pennapps filter
python filter_proj_fields.py proj/pennapps.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/pennapps/pennapps.json 1

#MHacks filter
python filter_proj_fields.py proj/mhacks.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/mhacks/mhacks.json 1

#HackGT filter
python filter_proj_fields.py proj/hackgt.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hackgt/hackgt.json 1

#Hack Texas filter
python filter_proj_fields.py proj/hacktx.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hacktx/hacktx.json 1

#USC filter
python filter_proj_fields.py proj/hacksc.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hacksc/hacksc.json 1

#Rutgers filter
python filter_proj_fields.py proj/hackru.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hackru/hackru.json 1

#Hack the north filter
python filter_proj_fields.py proj/hacknorth.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hacknorth/hacknorth.json 1

#Yale hack filter
python filter_proj_fields.py proj/yhack.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/yhack/yhack.json 1

#cornell
python filter_proj_fields.py proj/cornell.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/cornell/cornell.json 1

#Projects file filter
python filter_proj_fields.py proj/proj.json class_name,tagline,slug,photo,has_video proj_data/proj.json 1

#Filter the user data noise
python filter_proj_fields.py proj/user_data.json avatar_url proj_data/user_data.json 2

###############Extract data scripts

#Get tags from the projects
python filter_tags.py proj_data/proj.json proj_data/tags.csv 1

#Get project tags with true false. The last parameter determines the the minimum count of a tag to be extracted
python filter_tags.py proj_data/proj.json proj_data/tags_true.csv 2 200

#Get project tags with members weightage count
python filter_tags.py proj_data/proj.json proj_data/tags_true_cumu.csv 3 200 proj_data/user_data.jsondict.json


#Get all project tags with their count. CSC used for generating a tag cloud. The final number is the minimum count of projects in which the tags occur
python filter_tags.py proj_data/proj.json proj_data/aall_tags.csv 4 100


#Get all project tags with their count. CSC used for generating a tag cloud. The final number is the minimum count of projects in which the tags occur
python filter_tags.py proj_data/proj.json proj_data/aall_win_tags.csv 5 20


#Get project tags with members weightage count. The final number is the minimum count of projects in which the tags occur
python filter_tags.py proj_data/proj.json proj_data/tags_plot.csv 6 100

#Extract location data of various hackathons
python filter_user_data.py proj_data/calhacks/calhacks.json proj_data/user_data.jsondict.json proj_data/calhacks/loc.txt
python filter_user_data.py proj_data/pennapps/pennapps.json proj_data/user_data.jsondict.json proj_data/pennapps/loc.txt
python filter_user_data.py proj_data/mhacks/mhacks.json proj_data/user_data.jsondict.json proj_data/mhacks/loc.txt
python filter_user_data.py proj_data/techcrunch/techcrunch.json proj_data/user_data.jsondict.json proj_data/techcrunch/loc.txt
python filter_user_data.py proj_data/hackgt/hackgt.json proj_data/user_data.jsondict.json proj_data/hackgt/loc.txt
python filter_user_data.py proj_data/hacksc/hacksc.json proj_data/user_data.jsondict.json proj_data/hacksc/loc.txt
python filter_user_data.py proj_data/hacktx/hacktx.json proj_data/user_data.jsondict.json proj_data/hacktx/loc.txt
python filter_user_data.py proj_data/hacknorth/hacknorth.json proj_data/user_data.jsondict.json proj_data/hacknorth/loc.txt
python filter_user_data.py proj_data/yhack/yhack.json proj_data/user_data.jsondict.json proj_data/yhack/loc.txt
python filter_user_data.py proj_data/hackru/hackru.json proj_data/user_data.jsondict.json proj_data/hackru/loc.txt
python filter_user_data.py proj_data/cornell/cornell.json proj_data/user_data.jsondict.json proj_data/cornell/loc.txt

#Winner location
python filter_user_win_location.py proj_data/mhacks/mhacks.json proj_data/user_data.jsondict.json proj_data/pennapps/win_mhacks.txt
python filter_user_win_location.py proj_data/pennapps/pennapps.json proj_data/user_data.jsondict.json proj_data/mhacks/win_pennapps.txt
python filter_user_win_location.py proj_data/proj.json proj_data/user_data.jsondict.json proj_data/win_loc.txt
python filter_user_data.py proj_data/proj.json proj_data/user_data.jsondict.json proj_data/all_loc.txt


#Winner by state
python loc_scrap.py proj_data/all_loc.txt proj_data/win_loc.txt proj_data/loc_state.csv proj_data/map_density_plot/hack_data.js
