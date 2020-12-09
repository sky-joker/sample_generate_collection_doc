#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: sample_collection_doc
short_description: sample collection doc module
author:
  - sky-joker (@sky-joker)
description:
  - This module does nothing
requirements:
  - python >= 2.7
options:
  param1:
    description:
      - This parameter can be anything.
    type: str
    default: hoge
  param2:
    description:
      - This parameter can be anything.
    type: str
    default: fuga
  param3:
    description:
      - This parameter can be anything.
    type: str
    default: hogefuga
'''

EXAMPLES = r'''
- name: test
  sample_collection_doc:
    param1: hoge
'''

RETURN = r'''
param1:
  description: param1 value
  returned: always
  type: str
  sample: hoge
param2:
  description: param2 value
  returned: always
  type: str
  sample: fuga
param3:
  description: param3 value
  returned: always
  type: str
  sample: hogefuga
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = dict(
        param1=dict(type='str', default='hoge'),
        param2=dict(type='str', default='fuga'),
        param3=dict(type='str', default='hogefuga')
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    param1 = module.params.get('param1')
    param2 = module.params.get('param2')
    param3 = module.params.get('param3')

    result = dict(changed=False)
    result['param1'] = param1
    result['param2'] = param2
    result['param3'] = param3
    module.exit_json(**result)


if __name__ == "__main__":
    main()
