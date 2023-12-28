# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import sys
import json
import pandas as pd
import validators


def main(json_file, export_csv_path):

    df = pd.DataFrame([], columns=["title", "website", "username", "password", "notes", "last_used"])

    with open(json_file, 'r') as f:
        mpsites = json.load(f)

    i = 0
    for site, vs in mpsites['sites'].items():
        ne = [site]
        if validators.domain(site):
            ne.append(site)
        else:
            ne.append('')
        if 'login_name' in vs:
            ne.append(vs['login_name'])
        else:
            ne.append('')
        ne.append(vs['password'])
        # notes?
        ne.append('')
        if 'last_used' in vs:
            ne.append(vs['last_used'])
        else:
            ne.append('')
        df.loc[i] = ne
        i += 1

    df.to_csv(export_csv_path)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

