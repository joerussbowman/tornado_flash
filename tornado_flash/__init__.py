# -*- coding: utf-8 -*-
#
# Copyright 2011 Joseph Bowman
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


try: import simplejson as json
except ImportError: import json

class Flash(object):
    def __init__(self, req_obj):
        self.req_obj = req_obj

        self.cookie_name = "f"
        cookie = self.req_obj.get_secure_cookie(self.cookie_name)
        if cookie:
            self.__dict__["data"] = json.loads(cookie)
            self.req_obj.clear_cookie(self.cookie_name)
        else:
            self.__dict__["data"] = {}

    def __setattr__(self, name, value):
        if name == "data":
            self.__dict__["data"] = value
            self.req_obj.set_secure_cookie(self.cookie_name,
                    json.dumps(value))
        else:
            self.__dict__[name] = value


