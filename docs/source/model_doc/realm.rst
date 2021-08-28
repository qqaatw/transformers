.. 
    Copyright 2020 The HuggingFace Team. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
    the License. You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
    an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
    specific language governing permissions and limitations under the License.

REALM
-----------------------------------------------------------------------------------------------------------------------

Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The REALM model was proposed in `<INSERT PAPER NAME HERE>
<<INSERT PAPER LINK HERE>>`__  by <INSERT AUTHORS HERE>. <INSERT SHORT SUMMARY HERE>

The abstract from the paper is the following:

*<INSERT PAPER ABSTRACT HERE>*

Tips:

<INSERT TIPS ABOUT MODEL HERE>

This model was contributed by `<INSERT YOUR HF USERNAME HERE> 
<https://huggingface.co/<INSERT YOUR HF USERNAME HERE>>`__. The original code can be found `here 
<<INSERT LINK TO GITHUB REPO HERE>>`__.

RealmConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: transformers.RealmConfig
    :members:


RealmTokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: transformers.RealmTokenizer
    :members: build_inputs_with_special_tokens, get_special_tokens_mask,
        create_token_type_ids_from_sequences, save_vocabulary


RealmTokenizerFast
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: transformers.RealmTokenizerFast
    :members:


RealmModel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: transformers.RealmModel
    :members: forward


RealmForMaskedLM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: transformers.RealmForMaskedLM
    :members: forward