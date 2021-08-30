# coding=utf-8
# Copyright The HuggingFace Team and The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tokenization classes for REALM."""
from ...utils import logging
from ..bert.tokenization_bert import BertTokenizer


logger = logging.get_logger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "vocab.txt"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "realm-cc-news-pretrained-embedder": "https://huggingface.co/qqaatw/realm-cc-news-pretrained-embedder/resolve/main/vocab.txt",
        "realm-cc-news-pretrained-retriever": "https://huggingface.co/qqaatw/realm-cc-news-pretrained-retriever/resolve/main/vocab.txt",
        "realm-cc-news-pretrained-encoder": "https://huggingface.co/qqaatw/realm-cc-news-pretrained-encoder/resolve/main/vocab.txt",
    }
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "realm-cc-news-pretrained-embedder": 512,
    "realm-cc-news-pretrained-retriever": 512,
    "realm-cc-news-pretrained-encoder": 512
}


PRETRAINED_INIT_CONFIGURATION = {
    "realm-cc-news-pretrained-embedder": {"do_lower_case": True},
    "realm-cc-news-pretrained-retriever": {"do_lower_case": True},
    "realm-cc-news-pretrained-encoder": {"do_lower_case": True},
}


class RealmTokenizer(BertTokenizer):
    r"""
    Construct a REALM tokenizer.

    :class:`~transformers.RealmTokenizer` is identical to :class:`~transformers.BertTokenizer` and runs end-to-end
    tokenization: punctuation splitting and wordpiece.

    Refer to superclass :class:`~transformers.BertTokenizer` for usage examples and documentation concerning
    parameters.
    """

    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION