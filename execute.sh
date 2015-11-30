# Filter scripts

python filter_proj_fields.py proj/calhacks.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/calhacks/calhacks.json 1

python filter_proj_fields.py proj/techcrunch.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/techcrunch/techcrunch.json 1

python filter_proj_fields.py proj/pennapps.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/pennapps/pennapps.json 1

python filter_proj_fields.py proj/mhacks.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/mhacks/mhacks.json 1

python filter_proj_fields.py proj/hackgt.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hackgt/hackgt.json 1

python filter_proj_fields.py proj/hacktx.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hacktx/hacktx.json 1

python filter_proj_fields.py proj/hacksc.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hacksc/hacksc.json 1

python filter_proj_fields.py proj/hackru.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hackru/hackru.json 1

python filter_proj_fields.py proj/hacknorth.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/hacknorth/hacknorth.json 1

python filter_proj_fields.py proj/yhack.json class_name,name,tagline,slug,photo,has_video,like_count,comment_count proj_data/yhack/yhack.json 1

python filter_proj_fields.py proj/proj.json class_name,tagline,slug,photo,has_video proj_data/proj.json 1

###############Extract data scripts
python filter_tags.py proj_data/proj.json proj_data/tags.csv 1

#Get project tags with true false
python filter_tags.py proj_data/proj.json proj_data/tags_true.csv 2 200
python filter_proj_fields.py proj/user_data.json avatar_url proj_data/user_data.json 2
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