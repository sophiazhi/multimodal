# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import unittest

import torch
from torchmultimodal.models.flava import (
    flava_model_for_pretraining,
    flava_model_for_classification,
)


NUM_CLASSES = 2


class TestFLAVA(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(1234)

<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skip("Pending fix network connection, see (T116682215)")
=======
    @unittest.skip("dsds")
>>>>>>> 6fb41e7 ([fix,refactor] ImageNet HF support and fixes)
=======
    @unittest.skip("Pending fix network connection, see (T116682215)")
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)
    @torch.no_grad()
    def test_forward_classification(self):
        flava = flava_model_for_classification(NUM_CLASSES)
        text = torch.randint(0, 30500, (2, 77), dtype=torch.long)
        image = torch.rand((2, 3, 224, 224))

        labels = torch.randint(0, 2, (2,), dtype=torch.long)

        # Test multimodal scenario
        output = flava(image, text, "mm", labels)
<<<<<<< HEAD
<<<<<<< HEAD
        self.assertAlmostEqual(output.loss.item(), 0.9724, places=4)

        # Test unimodal image scenario
        output = flava(image, text, "image", labels)
        self.assertAlmostEqual(output.loss.item(), 0.5453, places=4)

        # Test unimodal text scenario
        output = flava(image, text, "text", labels)
        self.assertAlmostEqual(output.loss.item(), 0.7074, places=4)
=======
        self.assertTrue(
            torch.allclose(
                output.loss, torch.tensor(0.9303, dtype=torch.float), atol=1e-4
            )
        )
        self.assertTrue(
            torch.allclose(
                output.logits.sum(), torch.tensor(0.7676, dtype=torch.float), atol=1e-4
            )
        )
=======
        self.assertAlmostEqual(output.loss.item(), 0.9724, places=4)
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)

        # Test unimodal image scenario
        output = flava(image, text, "image", labels)
        self.assertAlmostEqual(output.loss.item(), 0.5453, places=4)

        # Test unimodal text scenario
        output = flava(image, text, "text", labels)
<<<<<<< HEAD
        self.assertTrue(
            torch.allclose(
                output.loss, torch.tensor(0.7074, dtype=torch.float), atol=1e-4
            )
        )
        self.assertTrue(
            torch.allclose(
                output.logits.sum(), torch.tensor(-1.0528, dtype=torch.float), atol=1e-4
            )
        )
>>>>>>> 6fb41e7 ([fix,refactor] ImageNet HF support and fixes)
=======
        self.assertAlmostEqual(output.loss.item(), 0.7074, places=4)
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)

    @unittest.skip("Pending fix network connection, see (T116682215)")
    @torch.no_grad()
    def test_forward_pretraining(self):
        flava = flava_model_for_pretraining()
        text = torch.randint(0, 30500, (2, 77), dtype=torch.long)
        image = torch.rand((2, 3, 224, 224))
        image_for_codebook = torch.rand(2, 3, 112, 112)
        image_patches_mask = torch.randint(0, 2, (2, 196), dtype=torch.long)
        text_masked = text.detach().clone()
        text_masked[:, 1:3] = 100
        mlm_labels = text.detach().clone()
        mlm_labels[:, :] = -1
        mlm_labels[:, 1:3] = text[:, 1:3]
        itm_labels = torch.tensor((0, 1), dtype=torch.long)

        output = flava(
            image=image,
            text=text,
            image_for_codebook=image_for_codebook,
            image_patches_mask=image_patches_mask,
            text_masked=text_masked,
            required_embedding="mm",
            itm_labels=itm_labels,
            mlm_labels=mlm_labels,
        )
        self.assertIsNone(output.mlm_output)
        self.assertIsNone(output.mim_output)
        self.assertIsNotNone(output.global_contrastive_output)
        self.assertIsNotNone(output.mmm_text_output)
        self.assertIsNotNone(output.mmm_image_output)
        self.assertIsNotNone(output.itm_output)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)
        self.assertAlmostEqual(
            sum(
                value if value is not None else 0 for value in output.losses.values()
            ).item(),
            20.4199,
            places=4,
<<<<<<< HEAD
=======
        print(output.itm_output)
        return
        self.assertTrue(
            torch.allclose(
                sum(
                    value if value is not None else 0
                    for _, value in asdict(output.losses).items()
                ),
                torch.tensor(20.6433, dtype=torch.float),
                atol=1e-4,
            )
>>>>>>> 6fb41e7 ([fix,refactor] ImageNet HF support and fixes)
=======
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)
        )

        output = flava(
            image=image,
            text=text,
            image_for_codebook=image_for_codebook,
            image_patches_mask=image_patches_mask,
            text_masked=text_masked,
            required_embedding="image",
            itm_labels=itm_labels,
            mlm_labels=mlm_labels,
        )
        self.assertIsNone(output.mlm_output)
        self.assertIsNotNone(output.mim_output)
        self.assertIsNone(output.global_contrastive_output)
        self.assertIsNone(output.mmm_text_output)
        self.assertIsNone(output.mmm_image_output)
        self.assertIsNone(output.itm_output)
        self.assertAlmostEqual(
            sum(
                value if value is not None else 0 for value in output.losses.values()
            ).item(),
            9.3403,
            places=4,
        )

        output = flava(
            image=image,
            text=text,
            image_for_codebook=image_for_codebook,
            image_patches_mask=image_patches_mask,
            text_masked=text_masked,
            required_embedding="text",
            itm_labels=itm_labels,
            mlm_labels=mlm_labels,
        )
        self.assertIsNotNone(output.mlm_output)
        self.assertIsNone(output.mim_output)
        self.assertIsNone(output.global_contrastive_output)
        self.assertIsNone(output.mmm_text_output)
        self.assertIsNone(output.mmm_image_output)
        self.assertIsNone(output.itm_output)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)
        self.assertAlmostEqual(
            sum(
                value if value is not None else 0 for value in output.losses.values()
            ).item(),
            10.8777,
            places=4,
<<<<<<< HEAD
=======
        self.assertTrue(
            torch.allclose(
                sum(
                    value if value is not None else 0
                    for _, value in asdict(output.losses).items()
                ),
                torch.tensor(10.8777, dtype=torch.float),
                atol=1e-4,
            )
>>>>>>> 6fb41e7 ([fix,refactor] ImageNet HF support and fixes)
=======
>>>>>>> b2a1f6a ([feat] Add support for configuration system along with README)
        )
